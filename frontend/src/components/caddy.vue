<template>
  <a-layout>
    <Header />
    <a-layout>

      <a-layout style="padding: 0 24px 24px">
        <a-breadcrumb style="margin: 16px 0">
          <a-breadcrumb-item>主页</a-breadcrumb-item>
          <a-breadcrumb-item>Caddy程序</a-breadcrumb-item>
        </a-breadcrumb>
        <a-layout-content :style="{ background: '#fff', padding: '24px', margin: 0, minHeight: '280px' }">
          <!-- 请注意，以下的示例包含超链接，您可能需要手动配置样式使其不变色。如果您嫌麻烦，可以移除。 -->
          <MonacoEdito ref="html"></MonacoEdito>
          <a-button type="primary" @click="upload_caddyfile">保存</a-button>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </a-layout>
</template>
<script type="ts">
import router from "../router";
import { defineComponent, ref, toRaw } from 'vue';
import cookies from "vue-cookies";
import axios from 'axios'
import MonacoEdito from "./monaco-editor.vue";
export default defineComponent({
  mounted: async function () {
    axios.get("/api/get_caddyfile").then(res => {
      this.code = res.data;
    })
  },
  methods: {
    async upload_caddyfile() {
      let token = cookies.get("token")
      const data = {
        token: token,
        text: toRaw(this.$refs.html.monacoEditor).getValue()
      }
      let response = await axios.post("/api/uploadtext", data)
    }
  },
  setup() {
    if (cookies.isKey("token") == false) {
      router.push("/login");
    }
    else if (cookies.isKey("token") == true) {
      axios.get(`/api/get_auth?user=${cookies.get("username")}&password=${cookies.get("token")}`).then(res => {
        if (res.data == "false") {
          router.push("/login");
        }
      });
    }
  },
  components: { MonacoEdito }
})
</script>