<template>
  <div class="bg">
<!--  添加Tab的面板  -->
    <q-dialog v-model="showAdd" :persistent="true">
      <AddTabCard v-model:tab-all="tabAll" v-model:tabs="tabs" v-model:show-add="showAdd"/>
    </q-dialog>

<!--  删除Tab的面板  -->
    <q-dialog v-model="showDel" :persistent="true">
      <DelTabCard v-model:tab-all="tabAll" v-model:tabs="tabs" v-model:show-del="showDel"/>
    </q-dialog>
    
<!--  修改壁纸的面板  -->
    <q-dialog v-model="showWall" :persistent="true">
      <WallpaperCard v-model:show-wall="showWall"/>
    </q-dialog>
    
    <Transition>
      <div class="bg-blur" v-if="isBlur"/>
    </Transition>
    <div class="row" style="z-index: 100; display: flex; justify-content: end; height: 1vh">
      <q-btn-group flat style="margin: 1vh">
        <q-btn flat color="primary" icon="edit" @click="showWall=true"/>
        <q-btn flat color="primary" icon="logout" @click="logout"/>
      </q-btn-group>
    </div>
    <div class="row" id="top-container">
<!--  资源监视器   -->
      <div class="col-md-6 col-sm-10 col-xs-10 offset-md-3 offset-sm-1 offset-xs-1"
          style="display: flex; flex-flow: column; align-self: center">
        <StatusWatcher style="z-index: 10"/>
        <div id="search-box">
          <q-input clearable borderless v-model="text" label="剪贴板中转站" @click="isBlur=true" @blur="isBlur=false" @keyup.enter="paste" @clear="clrPaste">
            <template v-slot:prepend>
              <q-icon name="content_paste"/>
            </template>
          </q-input>
          <q-dialog v-model="dialog" :position="'bottom'" no-focus seamless>
            <q-card style="width: 350px;" class="bg-positive">
              <q-card-section class="row items-center no-wrap">
                <div style="color: white"> 保存成功 </div>
              </q-card-section>
            </q-card>
          </q-dialog>
        </div>
      </div>
    </div>
    <div class="row" style="height: 20vh; align-content: end; justify-content: center; display: flex;">
      <div class="row" style=" z-index: 2">
        <q-btn-group flat>
          <q-btn flat color="primary" icon="add" @click="showAdd = true"/>
        </q-btn-group>
        <q-btn-group flat>
          <q-btn flat color="primary" icon="delete" @click="showDel = true"/>
        </q-btn-group>
        <q-btn-group flat>
          <q-btn flat color="primary" icon="apps" @click="expendPanel"/>
        </q-btn-group>
      </div>
    </div>
    <div class="row" style="height: 25vh; align-content: end; justify-content: center">
      <div class="col-lg-8 col-md-8 col-sm-11 col-xs-11" id="bottom-container">
        <div id="dock" :style="dockStyle">
          <div class="row" style="display: flex; width: 100%;">
            <div v-for="(tab, key) in tabs" :key="key" class="tab">
              <TabItem :tab="tab" class="icon"/>
            </div>
          </div>
        </div>
        <div v-if="isExpend" style="position: absolute; top: 0; left: 0; width: 100vw; height: 100vh" @click="shrinkPanel"/>
      </div>
    </div>
  </div>
</template>

<script>
import {defineComponent} from 'vue'
import {getTabs} from "src/api/tabsApi";
import TabItem from "components/TabItem.vue";
import {deletePaste, getPaste, setPaste} from "src/api/pasteApi";
import AddTabCard from "components/AddTabCard.vue";
import DelTabCard from "components/DelTabCard.vue";
import axios from "axios";
import WallpaperCard from "components/WallpaperCard.vue";
import StatusWatcher from "components/StatusWatcher.vue";

export default defineComponent({
  name: 'IndexPage',
  components: {StatusWatcher, WallpaperCard, DelTabCard, AddTabCard, TabItem},
  mounted() {
    this.getTabs();
    getPaste().then((resp) => {
      this.text = resp.data;
    });
  },
  data() {
    return {
      isBlur: false,
      isExpend: false,
      tabs: [],
      dockStyle: {
        height: "25vh",
        zIndex: 2
      },
      tabAll: [],
      background: "",
      text: "",
      showAdd: false,
      showDel: false,
      showWall: false,
      dialog: false
    }
  },
  methods: {
    paste() {
      setPaste(this.text).then((resp) => {
        if (resp.data.status === 'success') {
          this.dialog = true;
          setTimeout(() => {this.dialog = false}, 2000);
        }
      });
    },
    clrPaste() {
      this.text = "";
      deletePaste().then((resp) => {
        if (resp.data.status === 'success') {
          this.dialog = true;
          setTimeout(() => {this.dialog = false}, 2000);
        }
      });
    },
    logout() {
      localStorage.removeItem("Authorization");
      axios.defaults.headers.common["Authorization"] = "";
      this.$router.push("/login");
    },
    refreshTab() {
      this.tabs = [];
      for (let i = 0; i < (this.tabAll.length < 8 ? this.tabAll.length : 8); i++) {
        this.tabs.push(this.tabAll[i]);
      }
    },
    getTabs() {
      getTabs().then((resp) => {
        this.tabAll = resp.data;
        this.refreshTab();
      }).catch((err) => {
        if (err.response.status === 401) {
          this.$router.push("/login");
        }
      })
    },
    expendPanel() {
      let lineNum = this.tabAll.length / 4;
      if (lineNum <= 2) return;
      if (this.tabAll.length % 4 !== 0) {
        lineNum += 1;
      }
      this.dockStyle.height = lineNum * 12.375 + "vh";
      this.dockStyle.zIndex = 12;
      setTimeout(() => {
        for (let i = 8; i < this.tabAll.length; i++) {
          this.tabs.push(this.tabAll[i]);
        }
      }, 110)
      this.isExpend = true;
    },
    shrinkPanel() {
      this.dockStyle.height = "25vh"
      setTimeout(() => {this.dockStyle.zIndex = 2;}, 200)
      this.refreshTab();
      this.isExpend = false;
    },
  }
})
</script>
<style>
#top-container {
  height: 45vh;
  padding-top: 4vh;
}
#bottom-container {
  display: flex;
  align-content: center;
  justify-content: center;
  overflow: hidden;
  border-radius: 1rem;
}
#search-box {
  background-color: rgba(255, 255, 255, 0.45);
  border-radius: 5rem;
  padding-left: 3%;
  padding-right: 3%;
  -webkit-backdrop-filter: blur(20px);
  backdrop-filter: blur(20px);
  width: 100%;
  z-index: 10;
}
#dock {
  background-color: rgba(255, 255, 255, 0.15);
  -webkit-backdrop-filter: blur(20px);
  backdrop-filter: blur(20px);
  height: 25vh;
  width: 100%;
  padding: 1%;
  display: flex;
  align-items: center;
  z-index: 2;
  transition: height 0.2s ease-in-out;
  overflow-y: auto;
}
.bg {
  background: url('/wallpaper.png');
  height: 100vh;
  width: 100vw;
  background-size: cover;
  position: absolute;
  overflow: hidden;
}
.bg-blur {
  content: "";
  filter: blur(20px);
  position: absolute;
  background: inherit;
  background-size: inherit;
  z-index: 9;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  transform: scale(1.05);
}
.tab {
  margin: 1%;
  width: 23%;
  display: flex;
  justify-content: center;
}
.icon {
  transition: all 0.2s ease-in-out;
}
.icon:hover {
  transform: scale(1.3);
  z-index: 2;
}
.v-enter-active,
.v-leave-active {
  transition: opacity 0.16s ease-out;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
