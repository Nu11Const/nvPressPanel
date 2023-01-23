<template>
  <div>
    <a-button type="primary" @click="showModal">重启Docker服务</a-button>
    <a-modal v-model:visible="visible" title="重启Docker服务" @ok="handleOk">
      <p id="docker_restart_text"><a-spin /> 命令正在执行中,Please Wait......</p>
    </a-modal>
  </div>
</template>
<script type="js">
import { defineComponent, ref } from 'vue';
import axios from 'axios';
import cookies from 'vue-cookies'
export default defineComponent({
  setup() {
    const visible = ref(false);
    const showModal = () => {
      visible.value = true;
      let p = document.getElementById('docker_restart_text')
      let token = cookies.get("token")
      axios.get(`/api/restart_docker_service?token=${cookies.get("token")}`)
        .then(res => {
          var result = res.data;
          p.innerText = result;
        })
        .catch(err => {
          var error = 'error' + err;
        })
    };
    const handleOk = e => {
      console.log(e);
      visible.value = false;
    };
    return {
      visible,
      showModal,
      handleOk,
    };
  },
});
</script>