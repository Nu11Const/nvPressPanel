<template>
  <div>
    <a-button type="primary" @click="showModal">Docker状态</a-button>
    <a-modal v-model:visible="visible" title="Docker状态" @ok="handleOk">
      <p id="docker_status_text"><a-spin /> Loading...</p>
    </a-modal>
  </div>
</template>
<script type="js">
import { defineComponent, ref } from 'vue';
import axios from 'axios';
export default defineComponent({
  setup() {
    const visible = ref(false);
    const showModal = () => {
      visible.value = true;
      let p = document.getElementById('docker_status_text')
      axios.get("/api/get_docker_status")
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