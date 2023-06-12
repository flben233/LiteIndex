<script>
import {deleteTab} from "src/api/tabsApi";

export default {
  name: "DelTabCard",
  props: ['tabAll', 'tabs', 'showDel'],
  emits: ['update:tabAll', 'update:tabs', 'update:showDel'],
  mounted() {
    for (let item of this.tabAll) {
      this.tmpList.push(item);
    }
  },
  data() {
    return {
      tabDeleting: false,
      tmpList: [],
      tmpTabs: [],
      show: false,
      confirm: false,
      delTab: null
    }
  },
  methods: {
    refreshTab() {
      this.tmpTabs = [];
      for (let i = 0; i < (this.tmpList.length < 8 ? this.tmpList.length : 8); i++) {
        this.tmpTabs.push(this.tmpList[i]);
      }
      this.$emit("update:tabs", this.tmpTabs);
    },
    click(delTab) {
      this.delTab = delTab;
      this.confirm = true;
    },
    del() {
      let newList = [];
      for (let tab of this.tmpList) {
        if (tab.url === this.delTab.url && tab.icon === this.delTab.icon && tab.name === this.delTab.name) {
          continue;
        }
        newList.push(tab);
      }
      this.tmpList = newList;
      this.tabDeleting = true;
      deleteTab(this.delTab).then(() => {
        this.tabDeleting = false;
        this.refreshTab();
        this.$emit("update:tabAll", this.tmpList);
        this.confirm = false;
      })
    }
  }
}
</script>

<template>
    <q-card id="del">
      <q-dialog v-model="confirm" persistent>
        <q-card>
          <q-card-section class="row items-center">
            <span class="q-ml-sm">确定要删除吗？</span>
          </q-card-section>

          <q-card-actions align="right">
            <q-btn flat label="取消" color="primary" v-close-popup />
            <q-btn flat label="确定" color="negative" @click="del" :loading="tabDeleting"/>
          </q-card-actions>
        </q-card>
      </q-dialog>
      <q-card-section>
        <div class="text-h6">删除标签</div>
      </q-card-section>

      <q-card-section class="q-gutter-md" style="overflow: auto; max-height: 30vh">
        <q-list >
          <q-item clickable v-ripple v-for="(tab, key) in tmpList" :key="key" @click="click(tab)">
            <q-item-section avatar>
              <q-avatar text-color="white" color="teal">
                <q-img v-if="tab.icon!=null && tab.icon !== ''" :src=tab.icon />
                <div v-if="tab.icon==null || tab.icon === ''">{{tab.name.slice(0, 1)}}</div>
              </q-avatar>
            </q-item-section>
            <q-item-section>{{tab.name}}</q-item-section>
          </q-item>
        </q-list>
      </q-card-section>

      <q-card-actions align="right">
        <q-btn flat label="关闭" color="primary" v-close-popup/>
      </q-card-actions>
    </q-card>
</template>

<style scoped>
#del {
  border-radius: 1rem;
  @media screen and (min-width: 1281px) {
    width: 40vw;
  }
  @media screen and (max-width: 1280px) {
    width: 90vw;
  }
}
</style>