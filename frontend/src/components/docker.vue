<template>
    <a-layout>
    <Header/>
    <a-layout>
      <a-layout style="padding: 0 24px 24px">
        <a-breadcrumb style="margin: 16px 0">
          <a-breadcrumb-item>主页</a-breadcrumb-item>
          <a-breadcrumb-item>Docker程序</a-breadcrumb-item>
        </a-breadcrumb>
        <a-layout-content
          :style="{ background: '#fff', padding: '24px', margin: 0, minHeight: '280px' }"
        >
          <!-- 请注意，以下的示例包含超链接，您可能需要手动配置样式使其不变色。如果您嫌麻烦，可以移除。 -->
          <a-result
    status="success"
    title="Docker正常运行"
    sub-title="请点击下方按钮执行操作"
  >
    <template #extra>
      <div style="margin-left: 40%">
        <a-row :gutter="16">
          <Docker_status/>
          <Restart_docker_service style="margin-left: 1%"/>
        </a-row>
      </div>
      
    </template>
  </a-result>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </a-layout>
</template>
<script lang="js">
import router from "../router";
  import { defineComponent } from 'vue';
  import cookies from "vue-cookies";
import Docker_status from "./docker_status.vue";
import restart_docker_service from "./restart_docker_service.vue";
import Restart_docker_service from "./restart_docker_service.vue";
  export default defineComponent({
    setup() {
        if (cookies.isKey("user_logined") == false) {
            router.push("/login");
        }
    },
    components: { Docker_status, Restart_docker_service }
})
</script>