<template>
    <a-button type="primary" @click="setDark($event)">夜间模式</a-button>
</template>
<script>
import { defineComponent } from 'vue';
export const DarkMode = (isDark) => {
    if (isDark) {
        //import("../assets/theme/dark.less")
        changeCss("--page-bg-color", "#141414");
        changeCss("--head-bg-color", "rgba(0, 0, 0, 0.5)");
        changeCss("--line-color", "#2e2e2e");
        changeCss("--content-bg-color", "rgb(255 255 255 / 4%)");
        changeCss("--text-color", "rgba(255, 255, 255, 0.85)");
        changeCss("--silde-bg-color", "black");
        changeCss("--menu-color","black");
        changeCss("--ant-btn-color","#177ddc");
        changeCss("--font-color","white !important");
    } else {
        changeCss("--page-bg-color", "white");
        changeCss("--head-bg-color", "rgba(255, 255, 255, 0.7)");
        changeCss("--line-color", "#e8e8e8");
        changeCss("--content-bg-color", "#f0f2f5");
        changeCss("--text-color", "rgba(0, 0, 0, 0.85)");
        changeCss("--silde-bg-color", "#f0f2f5");
        changeCss("--menu-color","white");
        changeCss("--ant-btn-color","#1890ff");
        changeCss("--font-color","black !important");
    }
};
export const changeTheme = (theme) => {
    const head = document.head;
    document.getElementById("theme")?.remove();
    const styleDom = document.createElement("style");
    styleDom.id = "theme";
    styleDom.innerHTML = theme;
    head.appendChild(styleDom);
};

// 改变css变量
export const changeCss = (css, value) => {
    const body = document.body.style;
    body.setProperty(css, value);
};
export default defineComponent({
    methods: {
        setDark(e) {
            if (e.target.innerHTML === "夜间模式") {
                DarkMode(true);
                 e.target.innerHTML = "白昼模式";
            } else {
                DarkMode(false);
                e.target.innerHTML = "夜间模式";
            }

        }
    }
})
</script>