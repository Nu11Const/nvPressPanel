<template>
  <a-result status="error" title="nvPress未安装" sub-title="请检查您是否安装nvPress">
    <template #extra>
      <a-button key="console" type="primary" @click="showDrawer">去安装</a-button>
      <a-button key="buy">返回首页</a-button>
      <a-drawer v-model:visible="visible" class="custom-class" style="color: red" title="安装nvPress" placement="right"
        @after-visible-change="afterVisibleChange">
      </a-drawer>
    </template>
  </a-result>
</template>
<script lang="ts">
import { CloseCircleOutlined } from '@ant-design/icons-vue';
import { defineComponent, ref } from 'vue';
export default defineComponent({
  components: {
    CloseCircleOutlined,
  },
  setup() {
    const visible = ref<boolean>(false);
    const afterVisibleChange = (bool: boolean) => {
      console.log('visible', bool);
    };
    const showDrawer = () => {
      visible.value = true;
    };
    return {
      visible,
      afterVisibleChange,
      showDrawer,
    }
  }
});
</script>
<style scoped>
.desc p {
  margin-bottom: 1em;
}
</style>