<template>
  <a-result status="error" title="nvPress未安装" sub-title="请检查您是否安装nvPress">
    <template #extra>
      <a-button key="console" type="primary" @click="showDrawer">去安装</a-button>
      <a-button key="buy">返回首页</a-button>
      <a-drawer v-model:visible="visible" class="custom-class" style="color: red" title="安装nvPress" placement="right"
        @after-visible-change="afterVisibleChange">
        <a-button type="primary" block @click="install_nvpress">启动安装</a-button>
        <a-card :loading="loading" title="结果" style="margin-top: 10px" id="result_card">{{this.nvpress_install_status}}</a-card>
      </a-drawer>
    </template>
  </a-result>
</template>
<script lang="ts">
import { CloseCircleOutlined } from '@ant-design/icons-vue';
import { defineComponent, ref} from 'vue';
import axios from 'axios'
export default defineComponent({
  components: {
    CloseCircleOutlined,
  },
  mounted(){
    this.nvpress_install_status = "Waiting......."
  },
  setup() {
    const loading = ref(true);
    const handleClick = () => {
      loading.value = !loading.value;
    };
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
      loading,
      handleClick
    }
  },
  methods: {
    async install_nvpress(){
      let response = await axios.get(`/api/run_nvpress_docker_container?token=${this.$cookies.get("token")}`)
      this.handleClick()
      this.nvpress_install_status = response.data;
    },
  }
});
</script>
<style scoped>
.desc p {
  margin-bottom: 1em;
}
</style>