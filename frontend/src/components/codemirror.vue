<template>
  <div class="exercise">
    <codemirror v-model:value="codeSnippets" :options="cmOptions" />
  </div>
</template>

<script>
// 编辑器代码格式
import "codemirror/mode/javascript/javascript.js";
// 自动刷新(防止codemirror需要手动刷新才出数据)
import "codemirror/addon/display/autorefresh";
// 主题
import "codemirror/theme/ayu-mirage.css";
import { reactive, ref } from "vue";

export default {
  setup() {
    const codeSnippets = ref(`var i = 0;
for (; i < 9; i++) {
  console.log(i);
  // more statements
}`);
    const cmOptions = reactive({
      autorefresh: true,
      tabSize: 4,
      mode: "text/javascript",
      theme: "ayu-mirage",
      line: true,
      viewportMargin: Infinity, //处理高度自适应时搭配使用
      highlightDifferences: true,
      autofocus: false,
      indentUnit: 2,
      smartIndent: true,
      // readOnly: true, // 只读
      showCursorWhenSelecting: true,
      firstLineNumber: 1,
    });

    return { codeSnippets, cmOptions };
  },
};
</script>

<style lang="scss">
.CodeMirror {
  height: 100vh;
  direction: ltr;
}
</style>
