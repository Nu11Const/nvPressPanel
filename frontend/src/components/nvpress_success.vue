<template>
    <a-result title="您的nvPress已经成功配置！">
        <template #icon>
            <smile-twoTone />
        </template>
        <template #extra>
            <a-tooltip>
                <template #title>如您已经在安装时绑定域名，请使用域名访问，否则ip:11111
                    如无法访问请到nvPress界面确认状态
                </template>
                <a-button type="primary">如何访问？</a-button>
            </a-tooltip>
        </template>
    </a-result>
</template>
<script lang="ts">
import { SmileTwoTone } from '@ant-design/icons-vue';
import { defineComponent } from 'vue';
export default defineComponent({
    components: {
        SmileTwoTone,
    },
});
</script>

