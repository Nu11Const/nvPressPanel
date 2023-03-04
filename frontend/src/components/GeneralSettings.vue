<template>
    <a-collapse :default-active-key="['1', 2]">
        <a-collapse-item header="执行命令" key="1">

        </a-collapse-item>
        <a-collapse-item header="修改端口" :key="2">
            <a-form :model="form" @submit="handleSubmit">
                <a-form-item field="port" label="端口">
                    <a-input-number v-model="form.port" placeholder="" />
                </a-form-item>
                <a-form-item>
                    <a-button html-type="submit">提交</a-button>
                </a-form-item>
            </a-form>
        </a-collapse-item>
    </a-collapse>
</template>
<script>
import { reactive } from 'vue';

export default {
    setup() {
        const form = reactive({
            port: ''
        });
        const handleSubmit = (data) => {
            
        };

        return {
            form,
            handleSubmit,
        };
    },
};
</script>