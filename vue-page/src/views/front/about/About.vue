<template>
  <!-- <div> -->
  <!-- <card-img imgUrl="https://madmalls.com/api/medias/uploaded/chu-shou-wang-zhan-yuan-ma-f5bafb24.jpg"></card-img> -->
  <!-- </div> -->
  <about-content :content="aboutContent"></about-content>
</template>

<script>
import CardImg from "components/front/common/cardimg/CardImg";
import AboutContent from "./AbouContent";
import { request } from "network/request.js";
export default {
  metaInfo: {
    title: "关于作者", // set a title
    meta: [
      {
        // set meta
        name: "HUIHUIDEHUI 分享 python java vue linux 开发 机器学习",
        content:
          "HUIHUIDEHUI 本网站主要分享个人工作学习心得，包括python爬虫/机器学习/web开发/flask/、前端框架vue使用等相关知识，欢迎大家评论点赞！"
      },
      {
        name:"HUIHUIDEHUI about",
        content:"HUIHUIDEHUI python flask java vue linux"
      }
    ],
    link: [
      {
        // set link
        rel: "asstes",
        href: "http://www.huihuidehi.top/about"
      }
    ]
  },

  name: "About",
  data() {
    return {
      aboutContent: ""
    };
  },
  components: {
    // CardImg
    AboutContent
  },
  created() {
    this.getData();
  },
  methods: {
    getData() {
      request({
        url: "/about",
        method: "get"
      }).then(res => {
        // console.log(res)
        this.aboutContent = res.data.content;
      });
    }
  }
};
</script>

<style scoped>
</style>
