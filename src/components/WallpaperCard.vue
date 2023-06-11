<script>

import {uploadWallpaper} from "src/api/extensionApi";

export default {
  name: "WallpaperCard",
  props: ['showWall'],
  emits: ['update:showWall'],
  data() {
    return {
      uploading: false,
      imgFile: null,
      show: false
    }
  },
  methods: {
    upload() {
      this.uploading = true;
      uploadWallpaper(this.imgFile).then(() => {
        this.uploading = false;
        this.$emit("update:showWall", this.show);
        location.reload();
      })
    }
  }
}
</script>

<template>
  <q-card id="wall">
    <q-card-section class="q-gutter-md" style="overflow: auto; max-height: 30vh">
      <div class="text-h6">壁纸设置</div>
    </q-card-section>
    
    <q-card-section class="q-gutter-md" style="overflow: auto; max-height: 30vh">
      <q-file rounded standout="bg-primary text-white" v-model="imgFile" label="上传壁纸"/>
    </q-card-section>

    <q-card-actions align="right">
      <q-btn flat label="关闭" color="primary" v-close-popup/>
      <q-btn flat label="上传" color="primary" @click="upload" :loading="uploading"/>
    </q-card-actions>
  </q-card>
</template>

<style scoped>
#wall {
  width: 40vw;
  border-radius: 1rem;
  @media screen and (max-width: 1280px) {
    width: 80vw;
  }
}
</style>