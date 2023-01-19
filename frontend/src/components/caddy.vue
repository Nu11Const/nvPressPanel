<template>
    <a-layout>
    <Header/>
    <a-layout>
      
      <a-layout style="padding: 0 24px 24px">
        <a-breadcrumb style="margin: 16px 0">
          <a-breadcrumb-item>主页</a-breadcrumb-item>
          <a-breadcrumb-item>Caddy程序</a-breadcrumb-item>
        </a-breadcrumb>
        <a-layout-content
          :style="{ background: '#fff', padding: '24px', margin: 0, minHeight: '280px' }"
        >
          <!-- 请注意，以下的示例包含超链接，您可能需要手动配置样式使其不变色。如果您嫌麻烦，可以移除。 -->
          <monaco
        ref="monaco"
        :opts="opts"
        :height="500"
        :code="code"
      ></monaco>
      <a-button type="primary" @click="upload_caddyfile">保存</a-button>

        </a-layout-content>
      </a-layout>
    </a-layout>
  </a-layout>
</template>
<script>
import monaco from '../components/manaco.vue'
import router from "../router";
import axios from 'axios'
  import { defineComponent } from 'vue';
  import cookies from "vue-cookies";
  export default defineComponent({
    components: { monaco },
    mounted(){
      this.init()
    },
    methods: {
      init(){
        axios.get("/api/get_caddyfile").then(res=>{
          this.$refs.monaco.opts.value = res.data;
        })
      },
      upload_caddyfile(){
        var text = this.$refs.monaco.getVal();
        console.log(text);
        let url = `/api/uploadtext?text=${text}`
        axios.get(url)
      },
    },
    data () {
    return {
      sets: {
        language: {
          'apex': 'apex',
          'azcli': 'azcli',
          'bat': 'bat',
          'c': 'c',
          'clojure': 'clojure',
          'coffeescript': 'coffeescript',
          'cpp': 'cpp',
          'csharp': 'csharp',
          'csp': 'csp',
          'css': 'css',
          'dockerfile': 'dockerfile',
          'fsharp': 'fsharp',
          'go': 'go',
          'graphql': 'graphql',
          'handlebars': 'handlebars',
          'html': 'html',
          'ini': 'ini',
          'java': 'java',
          'javascript': 'javascript',
          'json': 'json',
          'kotlin': 'kotlin',
          'less': 'less',
          'lua': 'lua',
          'markdown': 'markdown',
          'msdax': 'msdax',
          'mysql': 'mysql',
          'objective-c': 'objective-c',
          'pascal': 'pascal',
          'perl': 'perl',
          'pgsql': 'pgsql',
          'php': 'php',
          'plaintext': 'plaintext',
          'postiats': 'postiats',
          'powerquery': 'powerquery',
          'powershell': 'powershell',
          'pug': 'pug',
          'python': 'python',
          'r': 'r',
          'razor': 'razor',
          'redis': 'redis',
          'redshift': 'redshift',
          'ruby': 'ruby',
          'rust': 'rust',
          'sb': 'sb',
          'scheme': 'scheme',
          'scss': 'scss',
          'shell': 'shell',
          'sol': 'sol',
          'sql': 'sql',
          'st': 'st',
          'swift': 'swift',
          'tcl': 'tcl',
          'typescript': 'typescript',
          'vb': 'vb',
          'xml': 'xml',
          'yaml': 'yaml'
        },
        theme: {
          'vs': 'vs',
          'vs-dark': 'vs-dark',
          'hc-black': 'hc-black'
        }
      },
      opts: {
        value: "hhh",
        readOnly: false, // 是否可编辑
        language: 'javascript', // 语言类型
        theme: 'vs-dark' // 编辑器主题
      }
    }
  },
    setup(){
      if(cookies.isKey("user_logined") == false){
        router.push("/login");
      }
    }
  })
</script>