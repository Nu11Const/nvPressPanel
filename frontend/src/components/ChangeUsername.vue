<template>
    <a-button @click="handleClick" type="primary">修改用户名</a-button>
    <a-modal v-model:visible="visible" @ok="handleOk" @cancel="handleCancel">
        <template #title>
            修改用户名
        </template>
        <a-form :model="form"  @submit="handleSubmit">
            <a-form-item field="newname" label="新名字">
                <a-input v-model="form.newname" placeholder="请输入新名字" />
            </a-form-item>
            <a-form-item>
                <a-button html-type="submit">提交</a-button>
            </a-form-item>
        </a-form>
    </a-modal>
</template>
  
<script>
import { reactive } from 'vue';
import { ref } from 'vue';
import axios from "axios"
import { Notification } from '@arco-design/web-vue'
import '@arco-design/web-vue/es/notification/style/css.js'
import { useRoute, useRouter } from 'vue-router'
export default {
    setup() {
        const route = useRoute()
        const router = useRouter()
        const visible = ref(false);
        const form = reactive({
            newname: '',
        });
        const handleSubmit = (data) => {
            console.log(data);
            axios.post("/api/auth/change_username",{
                newname: data["values"]["newname"]
            }).then(res => {
                router.push("/auth/logout")
            }).catch(error => Notification.error({
                title: '错误',
                content: error['message'],
                closable: true,
            }))
        };
        const handleClick = () => {
            visible.value = true;
        };
        const handleOk = () => {
            visible.value = false;
        };
        const handleCancel = () => {
            visible.value = false;
        }

        return {
            visible,
            handleClick,
            handleOk,
            handleCancel,
            form,
            handleSubmit,
        }
    },
}
</script>
