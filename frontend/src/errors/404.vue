<template>
    <a-result status="404" title="404" sub-title="Sorry, the page you visited does not exist.">
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