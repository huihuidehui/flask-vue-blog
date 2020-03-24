<template>
  <!-- <div class="home container column is-four-fifths-widescreen"> -->
  <!--  <div class="container column is-four-fifths-widescreen">-->
  <div class="tile is-ancestor">
    <div class="tile is-vertical is-parent is-9">
      <div class="tile is-child left">
        <blog-post-panel>
          <post-card v-for="article in articles" v-bind:key="article.id" :article="article"></post-card>
        </blog-post-panel>

        <pagination :toUrl="'tag/post/' +tagId" :totalPage="totalPage" :currentPage="currentPage"></pagination>
      </div>
    </div>
    <div class="tile is-parent">
      <div class="tile is-child">
        <aside>
          <blog-sider></blog-sider>
        </aside>
      </div>
    </div>
    <!--    </div>-->
  </div>
</template>

<script>
import BlogSider from "components/front/content/BlogSider";
import PostCard from "components/front/common/postcard/PostCard";
import Pagination from "components/front/common/pagination/Pagination";
import BlogPostPanel from "components/front/content/BlogPostPanel";
import { request } from "network/request.js";

export default {
  metaInfo() {
    return {
      title:
        this.tagName + " HUIHUIDEHUI 分享 python java vue linux 开发 机器学习", // set a title
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
        }
        // {
        // name: this.article.title,
        // content:this.article.abstract
        // }
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

  name: "TagPost",
  data() {
    return {
      totalPage: 0,
      currentPage: 0,
      articles: [],
      tagName: ""
    };
  },
  components: {
    BlogSider,
    BlogPostPanel,
    PostCard,
    Pagination
  },
  computed: {
    tagId() {
      return this.$route.params.tagId;
    }
  },
  watch: {
    $route() {
      this.getPostData();
    }
  },
  created() {
    // console.log(thi)
    // console.log(this.$router.params.page);
    this.getPostData();
    this.getTag();
  },
  methods: {
    getTag() {
      request({
        url: "/tag",
        method: "get",
        params: {
          id: this.$route.params.tagId
        }
      }).then(res => {
        this.tagName = res.data.name;
      });
    },

    getPostData() {
      request({
        url: "/tagposts",
        method: "get",
        params: {
          page: this.$route.params.page,
          id: this.$route.params.tagId
        }
      }).then(res => {
        if (res["res"] == 1) {
          // console.log(res)
          this.currentPage = res["currentPage"];
          this.totalPage = res["totalPage"];
          this.articles = res["data"];
        }
      });
    }
  },
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { x: 0, y: 0 };
    }
  }
};
</script>

<style scoped>
.pagination {
  padding-top: 1rem;
}

/* .home { */
/* padding-top: 2.5rem; */
/* } */
</style>
