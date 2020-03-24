<template>
  <div class="content" id="article">
    <div class="line-numbers markdown-body" v-html="htms"></div>
    <!-- <vue-markdown :source="content" :toc="true"></vue-markdown> -->
  </div>
</template>

<script>
import Prism from "prismjs";
import marked from "marked";
import "prismjs/themes/prism.css";
import "prismjs/plugins/toolbar/prism-toolbar.css";
import "prismjs/plugins/line-numbers/prism-line-numbers.css";

import AutocJs from "plugins/autoc.js";

let renderMD = new marked.Renderer();
marked.setOptions({
  renderer: renderMD,
  gfm: true,
  tables: true,
  breaks: false,
  pedantic: false,
  sanitize: false,
  smartLists: true,
  smartypants: false
});
// import VueMarkdown from "vue-markdown";

export default {
  props: ["content"],
  name: "PostContent",
  components: {
    // VueMarkdown
  },
  data() {
    return {
      htms: "",
      newContent: "",
      elelments: []
    };
  },
  watch: {
    content(val) {
      // 监测content值的变化
      this.newContent = val;
      this.setMakedown();
    }
  },
  updated() {
    // 当组件内容有更新时，进行代码高亮、渲染数学公式
    Prism.highlightAll();
    this.resume();

    // 创建目录
    let navigation = new AutocJs();
    // 可以在创建导航后，重置配置信息，重新生成新的导航
    // this.elelments = navigation.elelments
    // console.log(navigation.elelments)
    navigation.reload({
      // 调整位直接在文章内生成导航
      position: "outside",
      // 并且在文章标题前显示段落的章节层次索引值
      isGenerateHeadingChapterCode: false
    });
  },
  created() {
    // 配置mathjax
    this.create();
  },
  methods: {
    setMakedown() {
      this.htms = marked(this.newContent, { sanitize: true });
    },
    create() {
      MathJax.Hub.Config({
        tex2jax: {
          inlineMath: [
            ["$", "$"],
            ["\\(", "\\)"]
          ],
          displayMath: [
            ["$$", "$$"],
            ["\\[", "\\]"]
          ]
        }
      });
    },
    resume() {
      MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
    }
  }
};
</script>

<style scoped>
.content {
  margin-top: 1.5rem;
  margin-bottom: 1.5rem;
}

/* 覆盖bulma的样式 */
.content >>> .number {
  margin-right: 0px;
  background-color: transparent;
  display: unset;
  font-size: 100%;
  padding: 0px;
}
/* 调整代码字体大小以及背景，圆角 */
.content >>> pre {
  background: #f0f2f5;
  border-radius: 0.5rem;
  font-size: 14px;
  font-family: Consolas, Monaco, Menlo, Consolas, monospace;
  color: #34495e;
  text-shadow: none;
}
/* 去掉字体阴影 */
.content >>> code[class*="language-"] {
  text-shadow: none;
}
/* 去掉等号的背景 */
.content >>> .token.operator {
  background: none;
}

/* 覆盖sspai.css 对autocjs.css的影响 */
.content >>> .outline-outside-list {
  margin-left: 0px;
}
/* 引入目录相关的样式 */
@import "~assets/css/autocjs.css";
/* 引入markdown的样式 */
@import "~assets/css/sspai.css";
</style>
