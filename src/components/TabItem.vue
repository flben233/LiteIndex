<script>
  export default {
    name: "TabItem",
    props: ["tab"],
    methods: {
      jump(url) {
        window.open(url,'_blank');
      }
    },
    mounted() {
    }
  }
</script>

<template>
  <div style="display: flex; justify-content: center; flex-flow: column; ">
    <div style="justify-content: center; display: flex">
      <q-btn round @click="jump(tab.url)" style="width: fit-content">
        <q-avatar text-color="white" color="teal">
          <q-img v-if="tab.icon!=null && tab.icon !== ''" :src=tab.icon />
          <div v-if="tab.icon==null || tab.icon === ''">{{tab.name.slice(0, 1)}}</div>
        </q-avatar>
      </q-btn>
    </div>
    <div style="text-align: center; text-shadow: 2px 2px 2px #565555; color: white; font-weight: normal">{{tab.name}}</div>
  </div>
</template>

<style scoped>

</style>
