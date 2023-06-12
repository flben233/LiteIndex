<script>
import {uploadIcon, uploadTab} from "src/api/tabsApi";

export default {
  name: "AddTabCard",
  props: ['tabAll', 'tabs', 'showAdd'],
  emits: ['update:tabAll', 'update:tabs', 'update:showAdd'],
  mounted() {
    for (let item of this.tabAll) {
      this.tmpList.push(item);
    }
  },
  data() {
    return {
      tabName: "",
      tabUrl: "",
      tabIcon: "",
      iconUploading: false,
      tabUploading: false,
      iconFile: null,
      tmpList: [],
      tmpTabs: [],
      show: false
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
    async submit() {
      if (this.iconFile != null) {
        await uploadIcon(this.iconFile).then((resp) => {
          this.tabIcon = resp.data.url;
        });
      }
      let tab = {
        url: this.tabUrl.substring(0),
        name: this.tabName.substring(0),
        icon: this.tabIcon.substring(0)
      };
      this.tmpList.push(tab);
      this.tabUploading = true;
      uploadTab(tab).then(() => {
        this.tabUploading = false;
        this.refreshTab();
        this.$emit("update:tabAll", this.tmpList);
        this.$emit("update:showAdd", this.show);
      })
    }
  }
}
</script>

<template>
  <q-card id="dialog">
    <q-card-section>
      <div class="text-h6">添加标签</div>
    </q-card-section>

    <q-card-section class="q-gutter-md">
      <q-input rounded standout="bg-primary text-white" v-model="tabName" label="标签名字"/>
      <q-input rounded standout="bg-primary text-white" v-model="tabUrl" label="URL"/>
      <q-file rounded standout="bg-primary text-white" v-model="iconFile" label="上传图标" :loading="iconUploading"/>
    </q-card-section>

    <q-card-actions align="right">
      <q-btn flat label="关闭" color="primary" v-close-popup/>
      <q-btn flat label="提交" color="primary" @click="submit" :loading="tabUploading"/>
    </q-card-actions>
  </q-card>
</template>

<style scoped>
#dialog {
  border-radius: 1rem;
  padding: 0.5rem;
  @media screen and (min-width: 1281px) {
    width: 40vw;
  }
  @media screen and (max-width: 1280px) {
    width: 90vw;
  }
}
</style>