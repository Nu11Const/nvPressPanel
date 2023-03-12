<template>
    <a-layout style="padding: 0 24px;background: rgb(var(--gray-2))">
        <a-breadcrumb :style="{ margin: '16px 0' }">
            <a-breadcrumb-item>主页</a-breadcrumb-item>
            <a-breadcrumb-item>验证</a-breadcrumb-item>
            <a-breadcrumb-item>退出登录</a-breadcrumb-item>
        </a-breadcrumb>
        <a-layout-content style="color: var(--color-text-1)">
            <a-result status="success" title="退出成功">
                <template #extra>
                    <a-space>
                        <a-button type='primary' @click="returnhome">返回主页</a-button>
                    </a-space>
                </template>
            </a-result>
        </a-layout-content>
        <a-layout-footer style="color: var(--color-text-1)">Footer</a-layout-footer>
    </a-layout>
</template>
<script setup>
import { useRoute, useRouter } from 'vue-router'
const route = useRoute()
const router = useRouter()
$cookies.remove("token")
$cookies.remove("username")
function returnhome(){
    router.push("/auth/login")
}
</script>