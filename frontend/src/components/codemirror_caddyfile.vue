<template>
  <codemirror
    v-model="code"
    placeholder="Code gose here..."
    :style="{ height: '400px' }"
    :autofocus="true"
    :indent-with-tab="true"
    :tabSize="2"
    :extensions="extensions"
    @ready="setdata($event)"
    @change="setdata($event)"
    @focus="log('focus', $event)"
    @blur="log('blur', $event)"
    ref="code_mirror"
  />
  <a-button type="primary" @click="upload_caddyfile">保存</a-button>
</template>

<script>
import { Codemirror } from "vue-codemirror";
import { javascript } from "@codemirror/lang-javascript";
import { oneDark } from "@codemirror/theme-one-dark";
import axios from 'axios'
import { ref } from "vue";
import cookies from "vue-cookies";
export default {
  components: {
    Codemirror,
  },
  mounted() {
    this.init();
  },
  methods: {
    setdata(e){
      this.code_data = e;
    },
    get_data(){
      console.log(this.code_data);
    },
    async init() {
      let response = await axios.get("/api/get_caddyfile")
      this.code = response.data
    },
    async upload_caddyfile() {
      let token = cookies.get("token")
      console.log(this.code_data)
      const data = {
        token: token,
        text: this.code_data
      }
      let response = await axios.post("/api/uploadtext", data)
    }
  },
  setup() {
    let code = ref(``);
    const extensions = [javascript(), oneDark];
    function setcode(e){
      code = e;
    }
    return {
      code,
      extensions,
      log: console.log,
      setcode,
    };
  },
};
</script>
<style>
.cm-content {
  font-family: Consolas;
}
</style>