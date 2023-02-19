<template>
    <a-form :model="form" :style="{ width: '600px' }" @submit="handleSubmit">
        <a-form-item field="old-password" tooltip="请输入旧密码" label="旧密码">
            <a-input v-model="form.oldpassword" placeholder="请输入旧密码..." />
        </a-form-item>
        <a-form-item field="new-password" label="新密码">
            <a-input v-model="form.password" placeholder="请输入新密码..." />
        </a-form-item>
        <a-form-item>
            <a-button html-type="submit">提交</a-button>
        </a-form-item>
    </a-form>
    {{ form }}
    <ChangeUsername />
</template>
  
<script>
import { reactive } from 'vue';
import ChangeUsername from './ChangeUsername.vue';
export default {
    setup() {
        const form = reactive({
            oldpassword: "",
            password: "",
        });
        const handleSubmit = (data) => {
            console.log(data);
        };
        return {
            form,
            handleSubmit,
        };
    },
    components: { ChangeUsername }
};
</script>
  