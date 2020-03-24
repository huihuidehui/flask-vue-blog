<template>
  <!--  <div class="container column is-four-fifths-widescreen">-->
  <div class="tile is-ancestor">
    <div class="tile is-vertical is-parent is-9">
      <div class="tile is-child left">


        <div class="summary">
          <h2 class="is-size-5">
            目前共计{{totalPage}}文章
          </h2>
        </div>
        <div class="block">

          <el-timeline>
            <ul v-infinite-scroll="load" style="overflow:auto">
<!--              <li v-for="article in articles" :key="article.id">-->
                <el-timeline-item v-for="article in articles" :key="article.id"
                  :timestamp="getPostTime(article.postTime)"
                  :color="nodeColor"
                >
                  <h3 class="title is-size-6">{{article.title}}</h3>
                  <p>{{article.abstract}}</p>
                </el-timeline-item>
<!--              </li>-->
            </ul>
            <p v-if="loading">加载中...</p>
<!--            <p v-if="noMore">没有更多了</p>-->

          </el-timeline>

        </div>

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
  // import PostCard from "./childcpn/PostCard";

  import BlogSider from "components/front/content/BlogSider";
  import {request} from "network/request.js";
  import {formatDate} from "plugins/utils.js";

  export default {
    name: "Archive",
    data() {
      return {
        articles: [],
        totalPage: 1,
        nodeColor: "#00c582",
        page: 1,
        count: 0,
        loading: false,
      };
    },
    // computed: {
      // noMore() {
      //   return this.page > this.totalPage
      // }
    // },
    components: {
      BlogSider
    },
    created() {
      this.getData()
    },
    methods: {
      getData() {
        request({
          url: "/articles",
          method: 'get',
          params: {page: this.page}
        }).then(res => {
          if (res['res'] == 1) {
            this.articles = this.articles.concat(res['data']);
            this.totalPage = res['totalPage'];
            this.loading = false;
          }
        }).catch(err => {
        })
      },
      getPostTime(strTime) {
        return formatDate(strTime).toLocaleString();
      },
      load() {
        this.loading = true
        this.page += 1
        this.getData()
      }
    }
  };
</script>

<style scoped>
  .container {
    margin-top: 2rem;
  }

  .title {
    margin-bottom: 0.5rem;
    padding-top: 0.5rem;
  }

  .summary {
    /*margin-top: 2rem;*/
    margin-bottom: 2rem;
    color: #00c582;
  }
</style>
