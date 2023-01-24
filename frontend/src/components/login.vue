<template>
  <a-layout>
    <Header />
    <a-layout>
      <a-layout style="padding: 0 24px 24px">
        <a-breadcrumb style="margin: 16px 0">
          <a-breadcrumb-item>主页</a-breadcrumb-item>
          <a-breadcrumb-item>登录</a-breadcrumb-item>
        </a-breadcrumb>
        <a-layout-content :style="{ background: '#fff', padding: '24px', margin: 0, minHeight: '280px' }">
          <a-form :model="formState" name="basic" :label-col="{ span: 8 }" :wrapper-col="{ span: 16 }"
            autocomplete="off" @finish="onFinish" @finishFailed="onFinishFailed">
            <a-form-item label="用户名" name="username"
              :rules="[{ required: true, message: 'Please input your username!' }]">
              <a-input v-model:value="formState.username">
                <template #prefix>
                  <UserOutlined class="site-form-item-icon" />
                </template>
              </a-input>
            </a-form-item>

            <a-form-item label="密码" name="password"
              :rules="[{ required: true, message: 'Please input your password!' }]">
              <a-input-password v-model:value="formState.password">
                <template #prefix>
                  <LockOutlined class="site-form-item-icon" />
                </template>
              </a-input-password>
            </a-form-item>

            <a-form-item name="remember" :wrapper-col="{ offset: 8, span: 16 }">
              <a-checkbox v-model:checked="formState.remember">记住密码</a-checkbox>
            </a-form-item>

            <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
              <a-button type="primary" html-type="submit">登录</a-button>
            </a-form-item>
          </a-form>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </a-layout>
</template>
<script lang="ts">
//const sha256 = require("js-sha256").sha256; //引入sha256库
import { sha256 } from 'js-sha256'
import cookies from "vue-cookies";
import { defineComponent, reactive, ref } from 'vue';
import axios from 'axios'
import { useRouter } from 'vue-router';
import { message } from 'ant-design-vue';
import { UserOutlined, LockOutlined } from '@ant-design/icons-vue';
interface FormState {
  username: string;
  password: string;
  remember: boolean;
}
export default defineComponent({
  setup() {
    const router = useRouter();
    const visible = ref<boolean>(false);
    const visible1 = ref<boolean>(false);
    const handleClose = () => {
      visible.value = false;
    };
    const visible_error = ref<boolean>(false);
    const formState = reactive<FormState>({
      username: '',
      password: '',
      remember: true,
    });
    const onFinish = (values: any) => {
      var testvalue = Object.values(values);
      /*console.log('username:', testvalue[0]);
      console.log('password:', testvalue[1]);
      console.log('remember:',testvalue[2]);*/
      const content2 = testvalue[1];
      var hash = sha256('123456');
      let submmiturl = `/api/get_auth?user=${testvalue[0]}&password=${hash}`;
      axios.get(submmiturl)
        .then(res => {
          var result = res.data;
          //console.log(result);
          if (result == "true") {
            if (testvalue[2] == true) {
              cookies.set("token", hash, "7d")
              cookies.set("username", testvalue[0], "7d")
              message.success("登录成功")

              router.push({ path: "/" });

            } else if (testvalue[2] == false) {
              cookies.set("token", hash, "1d")
              cookies.set("username", testvalue[0], "1d")
              message.success("登录成功")

              router.push({ path: "/" });
            }
          } else {
            message.error("登录失败")
          }
        })
        .catch(err => {
          var error = 'error' + err;
        })
    };

    const onFinishFailed = (errorInfo: any) => {
      console.log('Failed:', errorInfo);
    };
    return {
      formState,
      onFinish,
      onFinishFailed,
      visible,
      handleClose,
      visible1,
    };
  },
});
</script>