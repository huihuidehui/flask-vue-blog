<template>
  <!-- <div>测试文章页面是否显示{{postUuid}}</div> -->
  <!--  <div class="container column is-four-fifths-widescreen">-->
  <div class="tile is-ancestor">
    <div class="tile is-vertical is-parent is-9">
      <div class="tile is-child left">
        <!-- <blog-post-panel> -->
        <!-- <post-card v-for="article in articles" v-bind:key="article.id" :article="article"></post-card> -->
        <!-- </blog-post-panel> -->
        <post>
          <template v-slot:PostTitle>
            <post-title
              v-bind:title="article.title"
              v-bind:viewNum="article.viewNum"
              v-bind:likeNum="article.likeNum"
              v-bind:postTime="postTime"
            ></post-title>
          </template>
          <template v-slot:PostImg>
            <post-img :abstract="article.abstract" :imgUrl="article.imgUrl"></post-img>
          </template>
          <template v-slot:PostContent>
            <post-content v-bind:content="article.content"></post-content>
          </template>

          <template v-slot:PostInfo>
            <post-info :article="article"></post-info>
          </template>
        </post>

      </div>
    </div>
    <div class="tile is-parent">
      <div class="tile is-child">
        <aside>
          <blog-sider></blog-sider>
        </aside>
      </div>
    </div>
  </div>
  <!--  </div>-->
</template>

<script>
import { request } from "network/request.js";
import BlogSider from "components/front/content/BlogSider";
import Post from "./childcpn/Post";
import PostTitle from "./childcpn/PostTitle";
import PostImg from "./childcpn/PostImg";
import PostContent from "./childcpn/PostContent";
import { formatDate } from "plugins/utils.js";
import PostInfo from "./childcpn/PostInfo";
export default {
  metaInfo() {
    return {
      title: this.article.title, // set a title
      meta: [
        {
          // set meta
          name: "HUIHUIDEHUI 分享 python java vue linux 开发 机器学习",
          content:
            "HUIHUIDEHUI 本网站主要分享个人工作学习心得，包括python爬虫/机器学习/web开发/flask/、前端框架vue使用等相关知识，欢迎大家评论点赞！"
        },
        {
          name: "HUIHUIDEHUI about",
          content: "HUIHUIDEHUI python flask java vue linux"
        },
        {
          name: this.article.title,
          content:this.article.abstract
        }
      ],
      link: [
        {
          // set link
          rel: "asstes",
          href: "http://www.huihuidehui.top" + this.$route.fullPath
        }
      ]
    };
  },

  name: "ShowPost",
  data() {
    return {
      postUuid: this.$route.params.postUuid,
      article: {}
    };
  },
  computed: {
    postTime() {
      return formatDate(this.article.postTime).toLocaleString();
    }
  },
  components: {
    PostContent,
    BlogSider,
    Post,
    PostTitle,
    PostImg,
    PostInfo
  },
  created() {
    // console.log("kanhui");
    this.getData();
  },
  watch: {
    $route() {
      this.getData();
    }
  },
  methods: {
    getData() {
      //
      // console.log("kanhu");
      request({
        url: "/article",
        method: "get",
        params: {
          uuid: this.$route.params.postUuid
        }
      }).then(res => {
        if (res["res"] == 1) {
          this.article = res["data"];
        }
      });
    }
  }
};
</script>

<style scoped>
</style>
