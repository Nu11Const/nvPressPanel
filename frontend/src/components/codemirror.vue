<template>
  <!-- :indent-with-tab="true" 是否自动获取焦点-->
  <codemirror v-model="code" placeholder="Code gose here..." :style="{ height: '70%' }" :autofocus="true"
      :tabSize="2" :extensions="extensions" :options="options" />
</template>
<!-- @ready="ready('ready', $event)"
      @change="Change('change', $event)" @focus="focus('focus', $event)" @blur="blur('blur', $event)" -->
<script lang="ts" setup>
import { Codemirror } from "vue-codemirror";
import { javascript } from "@codemirror/lang-javascript";
import { oneDark } from "@codemirror/theme-one-dark";
import { ref , reactive} from "vue";
import { EditorView } from "@codemirror/view"
import axios from "axios";
let myTheme = EditorView.theme({
  // 输入的字体颜色
  "&": {
      color: "#0052D9",
      backgroundColor: "#FFFFFF"
  },
  ".cm-content": {
      caretColor: "#0052D9",
  },
  // 激活背景色
  ".cm-activeLine": {
      backgroundColor: "#FAFAFA"
  },
  // 激活序列的背景色
  ".cm-activeLineGutter": {
      backgroundColor: "#FAFAFA"
  },
  //光标的颜色
  "&.cm-focused .cm-cursor": {
      borderLeftColor: "#0052D9"
  },
  // 选中的状态
  "&.cm-focused .cm-selectionBackground, ::selection": {
      backgroundColor: "#0052D9",
      color:'#FFFFFF'
  },
  // 左侧侧边栏的颜色
  ".cm-gutters": {
      backgroundColor: "#FFFFFF",
      color: "#ddd", //侧边栏文字颜色
      border: "none"
  }
}, { dark: true })
interface IProps {
  height?: string,
}

// 接受的参数
const props = withDefaults(defineProps<IProps>(), {
  height: '400px'
})
let code = ref();
const extensions = [javascript(), oneDark];
const Change = () => {

}
const options = reactive({
      style: { height: "400px" },
      mode: "text/x-c++src",
      spellcheck: true,
      autofocus: true,
      tabSize: 2,
      extensions: [oneDark], //传递给CodeMirror EditorState。创建({扩展})
      lineSeparator: 'a',
    });
</script>
