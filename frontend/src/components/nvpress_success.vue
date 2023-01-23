<template>
    <a-result title="Great, we have done all the operations!">
        <template #icon>
            <smile-twoTone />
        </template>
        <template #extra>
            <a-button type="primary">Next</a-button>
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

