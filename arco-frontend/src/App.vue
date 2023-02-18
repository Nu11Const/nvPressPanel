<template>
  <a-layout class="layout-demo" id="layout">
    <a-layout-sider hide-trigger collapsible :collapsed="collapsed">
      <div class="logo"><a href="/#/" style="" class="logo_a"><img src="/nvpress_logo.svg"></a></div>
      <a-menu :defaultOpenKeys="['1']" :defaultSelectedKeys="['0_3']" :style="{ width: '100%' }"
        @menuItemClick="onClickMenuItem">
        <a-menu-item key="/">
          <IconHome />
          主页
        </a-menu-item>
        <a-menu-item key="/docker">
          <IconCalendar />
          Docker
        </a-menu-item>
        <a-menu-item key="/ftp">
          <IconCalendar />
          FTP
        </a-menu-item>
        <a-menu-item key="/nvpress">
          <IconCalendar />
          nvPress
        </a-menu-item>
        <a-sub-menu key="4">
          <template #title>
            <span>
              <IconCalendar />系统设置
            </span>
          </template>
          <a-menu-item key="/settings/system">设置</a-menu-item>
          <a-menu-item key="/settings/docker">Docker设置</a-menu-item>
          <a-menu-item key="/settings/caddy">Caddy设置</a-menu-item>
          <a-menu-item key="/auth/logout">退出登录</a-menu-item>
        </a-sub-menu>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header style="padding-left: 20px;color: var(--color-text-1)">
        <a-button shape="round" @click="onCollapse">
          <IconCaretRight v-if="collapsed" />
          <IconCaretLeft v-else />
        </a-button>
        nvPressPanel - Dev
        <a-button type="primary" style="margin-left:70%" @click="darkMode($event)">暗黑模式</a-button>
      </a-layout-header>
      <router-view></router-view>
    </a-layout>
  </a-layout>
</template>
<script lang="js">
import { defineComponent, ref } from 'vue';
import { Message } from '@arco-design/web-vue';
import { IconMoonFill, IconCheckCircle } from '@arco-design/web-vue/es/icon';
import '@arco-design/web-vue/es/message/style/css.js'
import {
  IconCaretRight,
  IconCaretLeft,
  IconHome,
  IconCalendar,
  IconBulb
} from '@arco-design/web-vue/es/icon';
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
export default defineComponent({
  components: {
    IconCaretRight,
    IconCaretLeft,
    IconHome,
    IconCalendar,
    IconMoonFill,
    IconBulb
  },
  methods: {
    darkMode(e) {
      if (e.target.innerText === "暗黑模式") {
        e.target.innerText = "白昼模式";
        document.body.setAttribute('arco-theme', 'dark')
        window.localStorage.setItem('darkMode',"true");
      } else {
        e.target.innerText = "暗黑模式";
        document.body.removeAttribute('arco-theme');
        window.localStorage.setItem('darkMode',"false");
      }
    }
  },
  setup() {
    const route = useRoute()
    const router = useRouter()
    let flag = navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i)
    const collapsed = ref(false);
    if (flag){
      collapsed.value = ref(true);
    } else {
      collapsed.value = ref(false);
    }

    const onCollapse = () => {
      collapsed.value = !collapsed.value;
    };
    return {
      collapsed,
      onCollapse,
      onClickMenuItem(key) {
        router.push(key)
      },
      router,
      route
    };

  },
  async mounted() {
    if ($cookies.isKey("token") == false) {
      this.router.push("/auth/login")
    } else if ($cookies.isKey("token") == true) {
      let form = {
        "username": $cookies.get("username"),
        "password": $cookies.get("token")
      }
      try {
        let response = await axios.post("/api/auth/login", form)
        if (response.data["status"] == "403") {
          this.router.push("/auth/login")
        }
      } catch (error) {
        Message.error(error)
      }
    }
    try {
      if(window.localStorage.getItem("darkMode") == "true"){
        document.body.setAttribute('arco-theme', 'dark')
      } else {
        document.body.removeAttribute('arco-theme');
      }
    } catch(error) {
      console.log(`not have darkmode config,error:${error}`)
      window.localStorage.setItem("darkMode","false")
    }
  }
});
</script>
<style scoped>
.layout-demo {
  height: 500px;
  background: var(--color-fill-2);
  border: 1px solid var(--color-border);
}

.layout-demo :deep(.arco-layout-sider) .logo {
  height: 32px;
  margin: 12px 8px;
  background: rgba(255, 255, 255, 0.2);
}

.layout-demo :deep(.arco-layout-sider-light) .logo {
  background: var(--color-fill-2);
}

.layout-demo :deep(.arco-layout-header) {
  height: 64px;
  line-height: 64px;
  background: var(--color-bg-3);
}

.layout-demo :deep(.arco-layout-footer) {
  height: 48px;
  color: var(--color-text-2);
  font-weight: 400;
  font-size: 14px;
  line-height: 48px;
}

.layout-demo :deep(.arco-layout-content) {
  color: var(--color-text-2);
  font-weight: 400;
  font-size: 14px;
  background: var(--color-bg-3);
}

.layout-demo :deep(.arco-layout-footer),
.layout-demo :deep(.arco-layout-content) {
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: var(--color-white);
  font-size: 16px;
  font-stretch: condensed;
  text-align: center;
}

.logo_a[arco-theme='dark'] {
  color: white
}

.logo_a {
  color: var(--color-text-1);
  display: block;
  text-align: center;
  font-size: 20px;
  text-decoration: none;
}

body[arco-theme='dark'] {}
</style>

<style>
#app {
  height: 100vh;
}

body {
  margin: 0px;
}
</style>
