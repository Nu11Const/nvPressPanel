<template>
    <a-form :model="form" @submit="handleSubmit">
        <a-form-item field="old-password" tooltip="请输入旧密码" label="旧密码">
            <a-input-password v-model="form.oldpassword" placeholder="请输入旧密码..." />
        </a-form-item>
        <a-form-item field="new-password" label="新密码">
            <a-input-password v-model="form.password" placeholder="请输入新密码..." />
        </a-form-item>
        <a-form-item>
            <a-button html-type="submit">提交</a-button>
        </a-form-item>
    </a-form>
    <ChangeUsername />
</template>
  
<script>
import { reactive } from 'vue';
import ChangeUsername from './ChangeUsername.vue';
import axios from "axios"
import sha3, { sha3_256 } from 'js-sha3';
import { useRoute, useRouter } from 'vue-router'
import { Notification } from '@arco-design/web-vue'
import '@arco-design/web-vue/es/notification/style/css.js'
export default {
    setup() {
        const route = useRoute()
        const router = useRouter()
        const form = reactive({
            oldpassword: "",
            password: "",
        });
        const handleSubmit = (data) => {
            axios.post("/api/auth/change_password", {
                oldpassword: sha3.sha3_256(data["values"]["oldpassword"]),
                password: sha3.sha3_256(data["values"]["password"])
            }).then(res => {
                console.log(res)
                if (res["data"]["status"] == "403") {
                    Notification.error({
                        title: '错误',
                        content: "原密码错误",
                        closable: true,
                    })
                } else {
                    router.push("/auth/logout")
                }
            }).catch(error => Notification.error({
                title: '错误',
                content: error['message'],
                closable: true,
            }))
        };
        return {
            form,
            handleSubmit,
        };
    },
    components: { ChangeUsername }
};
</script>
<style>
.arco-input-wrapper {
    max-width: 60%;
}
</style>