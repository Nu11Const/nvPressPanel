<template>
  <a-layout class="layout-demo" id="layout">
      <a-layout-sider hide-trigger collapsible :collapsed="collapsed">
          <div class="logo"><a href="/#/" style="" class="logo_a"><img src="/nvpress_logo.svg"></a></div>
          <a-menu :defaultOpenKeys="['1']" :defaultSelectedKeys="['0_3']" :style="{ width: '100%' }"
              @menuItemClick="onClickMenuItem">
              <a-menu-item key="0_1">
                  <IconHome />
                  主页
              </a-menu-item>
              <a-menu-item key="0_2">
                  <IconCalendar />
                  Docker
              </a-menu-item>
              <a-menu-item key="0_3">
                  <IconCalendar />
                  FTP
              </a-menu-item>
              <a-menu-item key="0_4">
                  <IconCalendar />
                  nvPress
              </a-menu-item>
              <a-sub-menu key="4">
                  <template #title>
                      <span>
                          <IconCalendar />系统设置
                      </span>
                  </template>
                  <a-menu-item key="4_1">设置</a-menu-item>
                  <a-menu-item key="4_2">Docker设置</a-menu-item>
                  <a-menu-item key="4_3">Caddy设置</a-menu-item>
                  <a-menu-item key="4_4">退出登录</a-menu-item>
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
<script lang="ts">
import { defineComponent, ref } from 'vue';
import { Message } from '@arco-design/web-vue';
import { IconMoonFill, IconCheckCircle } from '@arco-design/web-vue/es/icon';
import {
  IconCaretRight,
  IconCaretLeft,
  IconHome,
  IconCalendar,
  IconBulb
} from '@arco-design/web-vue/es/icon';

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
      darkMode(e){
          if (e.target.innerText === "暗黑模式") {
               e.target.innerText = "白昼模式";
               document.body.setAttribute('arco-theme', 'dark')
          } else {
              e.target.innerText = "暗黑模式";
              document.body.removeAttribute('arco-theme');
          }
      }
  },
  setup() {
      const collapsed = ref(false);
      const onCollapse = () => {
          collapsed.value = !collapsed.value;
      };
      return {
          collapsed,
          onCollapse,
          onClickMenuItem(key) {
              Message.info({ content: `You select ${key}`, showIcon: true });
          }
      };
  },
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
