<template>
    <a-layout style="padding: 0 24px;background: rgb(var(--gray-2))">
        <a-breadcrumb :style="{ margin: '16px 0' }">
            <a-breadcrumb-item>主页</a-breadcrumb-item>
            <a-breadcrumb-item>设置</a-breadcrumb-item>
            <a-breadcrumb-item>系统设置</a-breadcrumb-item>
        </a-breadcrumb>
        <a-layout-content style="color: var(--color-text-1)">
            <a-tabs id="tab">
                <a-tab-pane key="1">
                    <template #title>
                        用户管理
                    </template>
                    <UserManager />
                </a-tab-pane>
                <a-tab-pane key="2">
                    <template #title>
                         Tab 2
                    </template>
                    Content of Tab Panel 2
                </a-tab-pane>
                <a-tab-pane key="3">
                    <template #title>
                         Tab 3
                    </template>
                    Content of Tab Panel 3
                </a-tab-pane>
            </a-tabs>

        </a-layout-content>
        <a-layout-footer style="color: var(--color-text-1)">Footer</a-layout-footer>
    </a-layout>
</template>
<script>
import { useRoute, useRouter } from 'vue-router'
import { Message } from '@arco-design/web-vue';
import '@arco-design/web-vue/es/message/style/css.js'
import axios from "axios"
import UserManager from '../components/UserManager.vue';
export default {
    setup() {
        const route = useRoute()
        const router = useRouter()
        return {
            route,
            router
        }
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
    }
}
</script>
<style>
#tab {
    height: 100vh;
}
</style>