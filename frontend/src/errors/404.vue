<template>
    <a-layout style="padding: 0 24px;background: rgb(var(--gray-2))">
    <a-breadcrumb :style="{ margin: '16px 0' }">
      <a-breadcrumb-item>错误</a-breadcrumb-item>
      <a-breadcrumb-item>404</a-breadcrumb-item>
    </a-breadcrumb>
    <a-layout-content style="color: var(--color-text-1)">
        <a-result status="404" subtitle="对不起，此网页不见了">
        <template #extra>
            <a-space>
                <a-button type="primary" @click="gethome">回到主页
                </a-button>
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
function gethome(){
    router.push("/")
}
</script>