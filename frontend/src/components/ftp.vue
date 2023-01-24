<template>
  <a-layout>
    <Header />
    <a-layout>

      <a-layout style="padding: 0 24px 24px">
        <a-breadcrumb style="margin: 16px 0">
          <a-breadcrumb-item>主页</a-breadcrumb-item>
          <a-breadcrumb-item>FTP程序</a-breadcrumb-item>
        </a-breadcrumb>
        <a-layout-content :style="{ background: '#fff', padding: '24px', margin: 0, minHeight: '280px' }">
          <!-- 请注意，以下的示例包含超链接，您可能需要手动配置样式使其不变色。如果您嫌麻烦，可以移除。 -->
          <a-result title="如您在安装中安装了FTP控件,可使用用户:nvpress,密码:123456登录服务器">
            <template #icon>
              <smile-twoTone />
            </template>
            <template #extra>
              <a-tooltip>
                <template #title>更改/www/nvpresspanel目录下的ftppass.txt，重启服务即可</template>
                <a-button type="primary">如何更改密码？</a-button>
              </a-tooltip>
              
            </template>
          </a-result>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </a-layout>
</template>
<script>
import router from "../router";
import { defineComponent } from 'vue';
import cookies from "vue-cookies";
import axios from 'axios'
import { SmileTwoTone } from '@ant-design/icons-vue';
export default defineComponent({
  components: {
    SmileTwoTone,
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
</script>