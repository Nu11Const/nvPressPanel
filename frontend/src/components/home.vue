<script setup>
import Header from "../components/header.vue"
</script>
<template>
  <a-layout>
    <Header />
    <a-layout>
      <a-layout>
        <a-layout-header :style="{ background: '#fff', padding: 0 }">
          <a-row type="flex">
            <a-breadcrumb style="margin: 16px 0;margin-left: 50px;">
            <a-rol>
              <a-breadcrumb-item>主页
              </a-breadcrumb-item>
            </a-rol>
          </a-breadcrumb>
          </a-row>
          <a-divider />
        </a-layout-header>
        <a-layout-content :style="{ margin: '24px 16px 0' }">
          <div class="content" :style="{ padding: '24px', background: '#fff', minHeight: '80vh' }">
            <p id="hitokoto">
              <a href="#" id="hitokoto_text" style="color:black; font-size: 35px;text-align:center;display: block;">:D
                获取中...</a>
            </p>
            <p></p>
          </div>
        </a-layout-content>
        <a-layout-footer style="text-align: center">
          <span>
            VMTask ©2021-2023 Created by FlyBox Studios
          </span>
        </a-layout-footer>
      </a-layout>
    </a-layout>
  </a-layout>
</template>
<script>
import Darkmode from "./Darkmode.vue";
import router from "../router";
import { defineComponent } from 'vue';
import cookies from "vue-cookies";
import axios from 'axios'
// 切换css
export default defineComponent({
  methods: {
    changetheme() {
      DarkMode(false);
      console.log("已切换为黑暗主题");
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
})
fetch('https://v1.hitokoto.cn')
  .then(response => response.json())
  .then(data => {
    const hitokoto = document.querySelector('#hitokoto_text')
    hitokoto.href = `https://hitokoto.cn/?uuid=${data.uuid}`
    hitokoto.innerText = data.hitokoto
  })
  .catch(console.error)
    //this.$cookies.set("login_status", "true", {expires: "7D"});
</script>

<style>

</style>