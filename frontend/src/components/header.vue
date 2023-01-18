<template>
<a-layout-sider
      breakpoint="lg"
      collapsed-width="0"
      @collapse="onCollapse"
      @breakpoint="onBreakpoint"
    >
      <div class="logo">
        <p style="color:white;display:block;text-align: center;font-size: 25px;">nvPressPanel</p>
      </div>
      <a-menu   :selectedKeys="[$route.path]"
 theme="dark" router-link mode="inline">
        <a-menu-item key="/nvpress">
          <user-outlined />
          <span class="nav-text" router-link>nvPress</span>
          <router-link to="/nvpress"></router-link>
        </a-menu-item>
        <a-menu-item key="/ftp">
          <video-camera-outlined />
          <span class="nav-text">FTP</span>
          <router-link to="/ftp"></router-link>
        </a-menu-item>
        <a-menu-item key="/docker">
          <upload-outlined />
          <span class="nav-text">Docker</span>
          <router-link to="/docker"></router-link>
        </a-menu-item>
        <a-menu-item key="/caddy">
          <user-outlined />
          <span class="nav-text">Caddy</span>
          <router-link to="/caddy"></router-link>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
</template>
<script lang="ts">
import { UserOutlined, VideoCameraOutlined, UploadOutlined } from '@ant-design/icons-vue';
import { defineComponent, ref } from 'vue';
export default defineComponent({
  components: {
    UserOutlined,
    VideoCameraOutlined,
    UploadOutlined,
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