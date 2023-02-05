<template>
  <a-layout-sider breakpoint="lg" collapsed-width="0" @collapse="onCollapse" @breakpoint="onBreakpoint" theme="light">
    <div class="logo">
        <a style="display:block;text-align: center;font-size: 20px;" href="/#/"> <img src="/nvpress_logo.svg"/> nvPressPanel</a>
    </div>
    <a-menu :selectedKeys="[$route.path]" theme="light" router-link mode="inline" style="margin-top:25px">
      <a-menu-item key="/nvpress">
        <icon-font type="icon-wangzhankaifa" />
        <span class="nav-text">nvPress</span>
        <router-link to="/nvpress"></router-link>
      </a-menu-item>
      <a-menu-item key="/ftp">
        <icon-font type="icon-ftp" />
        <span class="nav-text">FTP</span>
        <router-link to="/ftp"></router-link>
      </a-menu-item>
      <a-menu-item key="/docker">
        <icon-font type="icon-docker" />
        <span class="nav-text">Docker</span>
        <router-link to="/docker"></router-link>
      </a-menu-item>
      <a-menu-item key="/caddy">
        <icon-font type="icon-fuwuqi" />
        <span class="nav-text">Caddy</span>
        <router-link to="/caddy"></router-link>
      </a-menu-item>
      <a-menu-item @click="logout">
        <icon-font type="icon-tuichudenglu" />
        <span class="nav-text">退出登录</span>
      </a-menu-item>
    </a-menu>
    <Darkmode ></Darkmode>
  </a-layout-sider>
</template>
<script lang="ts">
import { createFromIconfontCN } from '@ant-design/icons-vue';
import Darkmode from './Darkmode.vue';
const IconFont = createFromIconfontCN({
  scriptUrl: '//at.alicdn.com/t/c/font_3868557_bfhkismrdf.js',
});
import { UserOutlined, VideoCameraOutlined, UploadOutlined } from '@ant-design/icons-vue';
import { defineComponent, ref } from 'vue';
export default defineComponent({
  methods: {
    logout() {
      this.$cookies.remove("token")
      this.$cookies.remove("username")
      this.$router.push("/login")
    },
    gohome() {
      this.$router.push("/")
    },
    setDarkMode() {
      DarkMode(false);
    }
  },
  components: {
    UserOutlined,
    VideoCameraOutlined,
    UploadOutlined,
    IconFont,
  },
  setup() {
    const onCollapse = (collapsed: boolean, type: string) => {
      console.log(collapsed, type);
    };

    const onBreakpoint = (broken: boolean) => {
      console.log(broken);
    };

    return {
      selectedKeys: ref<string[]>(['4']),
      onCollapse,
      onBreakpoint,
    };
  },
});
</script>
<style>
#components-layout-demo-responsive .logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}

.site-layout-sub-header-background {
  background: #fff;
}

.site-layout-background {
  background: #fff;
}

[data-theme='dark'] .site-layout-sub-header-background {
  background: #141414;
}

#components-layout-demo-top-side-2 .logo {
  float: left;
  width: 120px;
  height: 31px;
  margin: 16px 24px 16px 0;
  background: rgba(255, 255, 255, 0.3);
}

.ant-row-rtl #components-layout-demo-top-side-2 .logo {
  float: right;
  margin: 16px 0 16px 24px;
}

.site-layout-background {
  background: #fff;
}

.ant-layout {
  height: 100%
}
</style>