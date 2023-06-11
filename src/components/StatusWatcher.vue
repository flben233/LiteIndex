<script>
import {getPerformanceInfo} from "src/api/extensionApi";

export default {
  name: "StatusWatcher",
  mounted() {
    setInterval(() => this.updateInfo(), 5000)
  },
  data() {
    return {
      cpuUsage: 80,
      memoryUsage: 0.5,
      temperature: 0.3,
      upload: 0.1,
      download: 0.7
    }
  },
  methods: {
    updateInfo() {
      getPerformanceInfo().then((resp) => {
        this.cpuUsage = Number(resp.data.cpu_usage);
        this.memoryUsage = resp.data.memory_usage / resp.data.memory_total;
        this.temperature = resp.data.temperature / 100.0;
        this.upload = resp.data.net_upload.toFixed(1);
        this.download = resp.data.net_download.toFixed(1);
      })
    }
  }
}
</script>

<template>
  <div class="row" style="width: 100%; margin-bottom: 1vh;">
    <div class="col-md-6 col-sm-6 col-xs-12" style="display: flex; align-items: center">
      <q-circular-progress
        reverse
        :value="cpuUsage"
        size="80px"
        :thickness="0.6"
        color="info"
        center-color="grey-8"
        style="float: left;"
      />
      <div style="width: 60%; float: right; display: flex; flex-flow: column; align-content: center">
        <div style="display: inline-flex; align-content: center; margin-left: 15px; font-size: 12px">
          <div style="margin-right: 15px">
            <div class="text bg-pink-6">Mem(%)</div>
            <div class="text bg-secondary">Temp(℃)</div>
          </div>
          <div style="width: 100%; display: flex; flex-flow: column; align-content: space-between">
            <q-linear-progress rounded color="pink-6" :value="memoryUsage" class="progress"/>
            <q-linear-progress rounded color="secondary" :value="temperature" class="progress"/>
          </div>
        </div>
        <div style="display: flex; width: 100%;">
          <div class="tip bg-orange">Up: {{upload}} KB/s | Down: {{download}} KB/s</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.progress {
  height: 12px;
  margin-bottom: 4px;
  margin-top: 10px;
}
.text {
  font-size: 12px;
  padding: 3px;
  border-radius: 1rem;
  color: white;
  margin-top: 3px;
  text-align: center;
}
.tip {
  margin-left: 15px;
  font-size: 12px;
  margin-top: 3px;
  padding: 3px;
  border-radius: 1rem;
  color: white;
}
</style>