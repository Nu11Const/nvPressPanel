<template>
  <div class="code-editor">
    <textarea ref="textarea" />
  </div>
</template>

<script>
import CodeMirror from 'codemirror'
import 'codemirror/lib/codemirror.css'
// 主题样式
import 'codemirror/theme/monokai.css'   
import 'codemirror/theme/idea.css'
// 支持数据类型
import 'codemirror/mode/css/css.js'
import 'codemirror/mode/yaml/yaml.js'  
import 'codemirror/mode/xml/xml.js'  
import 'codemirror/mode/javascript/javascript.js'
// 数据校验
import 'codemirror/addon/lint/lint.js'
import '@/styles/lint.css'
// 这个是正常的引入，但我注释掉了是因为我想修改里面的部分内容，所以我拿出来了(之前这些文件在node-modules中)
// import 'codemirror/addon/lint/lint.css'
// import 'codemirror/addon/lint/yaml-lint.js'
// import 'codemirror/addon/lint/javascript-lint.js'
// import 'codemirror/addon/lint/json-lint.js'
import '@/utils/yaml-lint.js'
import '@/utils/javascript-lint.js'
import '@/utils/json-lint.js'
// 提示弹窗
import 'codemirror/addon/dialog/dialog.js'
import 'codemirror/addon/dialog/dialog.css'
// 搜索功能
import 'codemirror/addon/search/search.js'
import 'codemirror/addon/search/searchcursor.js'
import 'codemirror/addon/search/jump-to-line.js'
// 折叠功能
import 'codemirror/addon/fold/foldgutter.css'
import 'codemirror/addon/fold/foldcode.js'
import 'codemirror/addon/fold/brace-fold.js'
import 'codemirror/addon/fold/xml-fold.js'
// 滚动条
import 'codemirror/addon/scroll/simplescrollbars.css'
import 'codemirror/addon/scroll/simplescrollbars.js' 
// 代码高亮
import 'codemirror/addon/hint/show-hint.js'
import 'codemirror/addon/hint/show-hint.css'
import 'codemirror/addon/hint/javascript-hint.js'
import 'codemirror/addon/hint/xml-hint.js'
import 'codemirror/addon/hint/anyword-hint.js'
import 'codemirror/addon/hint/html-hint.js'
import 'codemirror/addon/hint/css-hint.js'
import 'codemirror/addon/selection/active-line.js'
// 全屏
import 'codemirror/addon/display/fullscreen.js'
import 'codemirror/addon/display/fullscreen.css'

// 引入js-yaml为codemirror提高语法检查核心支持
window.jsyaml = require('js-yaml') 
// 引入jsonlint为codemirror提高语法检查核心支持
import jsonlint from "jsonlint-mod";
window.jsonlint = require('jsonlint');
// 引入xml为codemirror提高语法检查核心支持
import '@/utils/xml-lint.js'

export default {
  name: 'codeEditor',
  // eslint-disable-next-line vue/require-prop-types
  props: {
    value:{
      type: Object | String,
      default: null
    },
    mode:{
      type: String,
      default: 'yaml'
    },
    readOnly: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      codeEditor: false,
    }
  },
  watch: {
    value(value) {
      const editorValue = this.codeEditor.getValue()
      if (value !== editorValue) {
        this.codeEditor.setValue(this.value)
      }
    },
  },
  mounted() {  
    this.initCodeEditor()  
  },
  methods: {
    initCodeEditor() {
      this.codeEditor = CodeMirror.fromTextArea(this.$refs.textarea, {  
        mode: this.mode,              // 语法model
        theme: 'idea',                // 编辑器主题
        lint: true,                   // 开启语法检查
        readOnly:this.readOnly,       // 是否只可读
        lineNumbers: true,            // 显示行号
        gutters: ['CodeMirror-lint-markers'],  // 语法检查器，可提示错误信息 
        indentUnit: 2,                // 缩进单位为2
        smartIndent: true,            // 自动缩进是否开启
        matchBrackets: true,          // 括号匹配
        lineWrapping: true,           // 自动换行
        tabSize: 2,
        styleActiveLine: true,        // 设置光标所在行高亮
        scrollbarStyle: 'overlay',
        fullScreenChange: true,       // 全屏
        indentWithSpaces: true,
          extraKeys: {
            "F11": function (cm) {
              cm.setOption("fullScreen", !cm.getOption("fullScreen"));
            },
            "Esc": function (cm) {
              if (cm.getOption("fullScreen")) cm.setOption("fullScreen", false);
            }
          }
      })
      this.codeEditor.setValue(this.value)
      this.codeEditor.on('change', (cm) => {
        this.$emit('changed', cm.getValue())
        this.$emit('input', cm.getValue())
    })
    },
    getValue() {
      return this.codeEditor.getValue()
    }
  }
}
</script>

<style scoped>
.code-editor{
  height: 100%;
  position: relative;
}
.code-editor >>> .CodeMirror {
  height: auto;
  min-height: 300px;
}
.code-editor >>> .CodeMirror-scroll{
  min-height: 300px;
}
.code-editor >>> .cm-s-rubyblue span.cm-string {
  color: #F08047;
}
</style>
