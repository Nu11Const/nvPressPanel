<template>
    <a-layout style="padding: 0 24px;background: rgb(var(--gray-2))">
                <a-breadcrumb :style="{ margin: '16px 0' }">
                    <a-breadcrumb-item>主页</a-breadcrumb-item>
                    <a-breadcrumb-item>应用</a-breadcrumb-item>
                </a-breadcrumb>
                <a-layout-content style="color: var(--color-text-1)">
                    <a-progress type="circle" :percent="percent" />
                    内存
                </a-layout-content>
                <a-layout-footer style="color: var(--color-text-1)">Footer</a-layout-footer>
            </a-layout>
</template>
<script>
import { ref } from 'vue';
import axios from 'axios'
export default {
  setup() {
    let percent = ref(0);

    function setpercent(n){
        console.log("test")
        percent.value = n
    }

    return {
      percent,
      setpercent
    }
  },
  async created() {
    let response = await axios.post("/api/get_performance");
    console.log(response.data["memory"] / 100);
    this.setpercent(response.data["memory"] / 100);

  }
}
</script>