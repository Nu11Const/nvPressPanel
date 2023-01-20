<template>
    <a-result status="403" title="403" sub-title="Sorry, you are not authorized to access this page.">
        <template #extra>
            <a-button type="primary" @click="get_home">Back Home</a-button>
        </template>
    </a-result>
</template>
<script>
import { defineComponent } from 'vue';
export default defineComponent({
    methods:{
        get_home() {
            this.$router.push("/")
        }
    },
})
</script>