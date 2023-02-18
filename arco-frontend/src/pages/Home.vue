<template>
  <a-layout style="padding: 0 24px;background: rgb(var(--gray-2))">
    <a-breadcrumb :style="{ margin: '16px 0' }">
      <a-breadcrumb-item>主页</a-breadcrumb-item>
      <a-breadcrumb-item>应用</a-breadcrumb-item>
    </a-breadcrumb>
    <a-layout-content style="color: var(--color-text-1)">
      <a-space class="performance">
        <a-progress type="circle" :percent="percent" size="large" />
        内存
        <a-progress type="circle" :percent="percent1" size="large" />
        CPU
      </a-space>
    </a-layout-content>
    <a-layout-footer style="color: var(--color-text-1)">Footer</a-layout-footer>
  </a-layout>
</template>
<script lang="js">
import { ref } from 'vue';
import axios from 'axios'
import { Notification } from '@arco-design/web-vue'
import '@arco-design/web-vue/es/notification/style/css.js'
export default {
  setup() {
    let percent = ref(0);
    let percent1 = ref(0);
    function setpercent(n) {
      percent.value = n
    }
    function setpercent1(n) {
      percent1.value = n
    }

    return {
      percent1,
      setpercent,
      percent,
      setpercent1
    }
  },
  methods: {
    async getProformance() {
      try {
        let response = await axios.post("/api/get_performance")
        this.setpercent(response.data["memory"] / 100);
        this.setpercent1(response.data["cpu"] / 100);

      } catch (error) {
        Notification.error({
          title: '错误',
          content: error['message'],
          closable: true,
        })
      }
    },
  },
  async mounted() {
    this.timer = window.setInterval(() => {
      setTimeout(() => {
        this.getProformance()
      }, 0)
    }, 3000)
  },
  destroyed() {
    window.clearInterval(this.timer)
  }



}
</script>
<style>
.performance {
  justify-content: center;

}
</style>
