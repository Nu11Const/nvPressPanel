<template>
  <a-layout>
    <Header />
    <a-layout>

      <a-layout style="padding: 0 24px 24px">
        <a-breadcrumb style="margin: 16px 0">
          <a-breadcrumb-item>主页</a-breadcrumb-item>
          <a-breadcrumb-item>nvPress主进程</a-breadcrumb-item>
        </a-breadcrumb>
        <a-layout-content :style="{ background: '#fff', padding: '24px', margin: 0, minHeight: '280px' }">
          <!-- 请注意，以下的示例包含超链接，您可能需要手动配置样式使其不变色。如果您嫌麻烦，可以移除。 -->
          <nvpress_error v-if="visible1" id="nvp_error"></nvpress_error>
          <nvpress_success v-if="visible2"/>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </a-layout>
</template>
<script>
import nvpress_error from "./nvpress_error.vue";
import router from "../router";
import { defineComponent, ref } from 'vue';
import cookies from "vue-cookies";
import Nvpress_error from "./nvpress_error.vue";
import nvpress_success from '../components/nvpress_success.vue'
import axios from 'axios'
export default defineComponent({
  async created() {
    let response = await axios.get("/api/get_container_install_status")
    console.log(response.data)
    if (String(response.data).indexOf("false") == -1) {
      this.visible2 = ref(true)
    } else if (String(response.data).indexOf("false") != -1) {
      this.visible1 = ref(true)
      console.log(this.visible1)
    } else {
      console.log("bug")
    }
  },
  data() {
    return {
      visible1: this.visible1,
      visible2: this.visible2
    }
  },
  setup() {
    if (cookies.isKey("token") == false) {
      router.push("/login");
    } else if (cookies.isKey("token") == true) {
      axios.get(`/api/get_auth?user=${cookies.get("username")}&password=${cookies.get("token")}`).then(res => {
        if (res.data == "false") {
          router.push("/login");
        }
      })
    }
  },
  components: { Nvpress_error }
})
</script>