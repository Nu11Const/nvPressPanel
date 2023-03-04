<template>
    <a-layout style="padding: 0 24px;background: rgb(var(--gray-2))">
        <a-breadcrumb :style="{ margin: '16px 0' }">
            <a-breadcrumb-item>主页</a-breadcrumb-item>
            <a-breadcrumb-item>设置</a-breadcrumb-item>
            <a-breadcrumb-item>Caddy</a-breadcrumb-item>
        </a-breadcrumb>
        <a-layout-content style="color: var(--color-text-1)">

        </a-layout-content>
        <a-layout-footer style="color: var(--color-text-1)">Footer</a-layout-footer>
    </a-layout>
</template>
<script>
import { useRoute, useRouter } from 'vue-router'
import { Message } from '@arco-design/web-vue';
import '@arco-design/web-vue/es/message/style/css.js'
import axios from "axios"
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