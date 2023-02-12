<template>
    <a-layout style="padding: 0 24px;background: rgb(var(--gray-2))">
        <a-breadcrumb :style="{ margin: '16px 0' }">
            <a-breadcrumb-item>主页</a-breadcrumb-item>
            <a-breadcrumb-item>验证</a-breadcrumb-item>
            <a-breadcrumb-item>登录</a-breadcrumb-item>
        </a-breadcrumb>
        <a-layout-content style="color: var(--color-text-1)">
            <a-form :model="form" :style="{ width: '600px' }" @submit="handleSubmit">
                <a-form-item field="name" tooltip="请输入用户名" label="用户名">
                    <a-input v-model="form.username" placeholder="请输入用户名..." />
                </a-form-item>
                <a-form-item field="password" label="密码">
                    <a-input v-model="form.password" placeholder="请输入密码..." />
                </a-form-item>
                <a-form-item>
                    <a-button html-type="submit">提交</a-button>
                </a-form-item>
            </a-form>
            {{ form }}
        </a-layout-content>
        <a-layout-footer style="color: var(--color-text-1)">Footer</a-layout-footer>
    </a-layout>

</template>
<script>
import { reactive } from 'vue';
import axios from 'axios'
import { Notification } from '@arco-design/web-vue'
import '@arco-design/web-vue/es/notification/style/css.js'
export default {
    setup() {
        const form = reactive({
            username: '',
            password: '',
        });
        const handleSubmit = (data) => {
            axios.post("/api/auth/login", data.values).then(res => {
                console.log(res)
                if (res.data["status"] == "403") {
                    Notification.warning({
                        title: '提醒',
                        content: "账号或密码错误",
                        closable: true,
                    })
                } else if (res.data["status"] == "200") {
                    Notification.success({
                        title: '提醒',
                        content: "登录成功",
                        closable: true,
                    })
                } else {
                    Notification.error({
                        title: '错误',
                        content: "未知错误",
                        closable: true,
                    })
                }
            }).catch(error => Notification.error({
                title: '错误',
                content: error['message'],
                closable: true,
            }))
        };

        return {
            form,
            handleSubmit,
        };
    },
};
</script>
