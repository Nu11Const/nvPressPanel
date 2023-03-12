<template>
    <a-button type="primary" @click="handleClick" style="margin-left:10%">任务</a-button>
    <a-drawer :width="340" :visible="visible" @ok="handleOk" @cancel="handleCancel" unmountOnClose>
        <template #title>
            任务
        </template>
        <a-list :style="{}" :virtualListProps="{
            height: 560,
        }" :data="list">
            <template #item="{ item, index }">
                <a-list-item :key="index">
                    <a-list-item-meta :title='"任务ID:"+item.id' :description="item.status">
                    </a-list-item-meta>
                </a-list-item>
            </template>
        </a-list>
    </a-drawer>
</template>
  
<script>
import { ref } from 'vue';
import axios from "axios"
export default {
    setup() {
        const visible = ref(false);

        const handleOk = () => {
            visible.value = false;
        };
        const handleCancel = () => {
            visible.value = false;
        }
        let list = [
            
        ]
        return {
            visible,
            handleOk,
            handleCancel,
            list
        }
    },
    methods: {
        async handleClick() {
            this.visible = true;
            let res = await axios.post("/api/task/tasks");
            console.log(res.data)
            this.list.values = res.data;
            console.log(this.list)
        }
    }
};
</script>
  