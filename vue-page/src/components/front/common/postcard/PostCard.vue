<template>
  <div class="card">
    <slot name="post-img">
      <!--      <card-img v-if="isExistImg"-->
      <!--                :imgUrl="article.imgUrl"></card-img>-->
      <card-img v-if="isExistImg" :imgUrl="article.imgUrl"></card-img>
    </slot>

    <div class="card-content">
      <div class="media">
        <div class="media-left">
          <figure class="image is-48x48">
            <!-- <img -->
            <!-- class="is-rounded" -->
            <!-- src="https://madmalls.com/static/main/images/avatar.jpg" -->
            <!-- alt="Placeholder image" -->
            <!-- /> -->
            <img
              class="is-rounded"
              src="~assets/img/avatars.jpg"
              alt="Placeholder image"
            />
          </figure>
        </div>
        <div class="media-content">
          <p class="author-title is-size-6">
            @Kan Hui
            <br />
            <span class="is-size-7">
              发布于
              <slot name="post-date">{{postTime}}</slot>
            </span>
          </p>
        </div>
      </div>
      <div class="content">
        <!-- <div class="title"> -->
        <div class="my-icon">
          <span class="icon is-small has-text-info">
            <i class="fa fa-align-left fa-lg"></i>
          </span>
        </div>
        <div class="title">
          <a>
            <slot name="post-title">
              <!-- <a v-on:click="showPost">{{article.title}}</a> -->
              <!-- <router-link :to="'/showpost/' + article.uuid.substr(1,6)">{{article.title}}</router-link> -->
              <router-link :to="'/showpost/' + article.uuid">{{article.title}}</router-link>
            </slot>
          </a>
        </div>
        <p>
          <slot name="post-abstract">{{article.abstract}}</slot>
        </p>
        <ul class="is-size-7">
          <li class="list-item">
            <el-tooltip effect="dark" content="分类" placement="top">
              <span class="list-icon">
                <i class="fa fa-tag has-text-info"></i>
                <slot name="category">
                  <!-- <a>{{article.category}}</a> -->
                  <router-link :to="'/category/post/'+article.categoryId +'/1'">{{article.category}}</router-link>
                </slot>
              </span>
            </el-tooltip>
          </li>
          <li class="list-item">
            <el-tooltip effect="dark" content="标签" placement="top">
              <span>
                <i class="fa fa-tags has-text-primary"></i>
                <slot name="tags">
                  <!-- <a v-for="tag in article.tags" v-bind:key="tag.id">{{tag.name}} ·</a> -->
                  <router-link
                    v-for="tag in article.tags"
                    v-bind:key="tag.id"
                    :to="'/tag/post/'+tag.tagId+'/1'"
                  >{{tag.name}} ·</router-link>
                </slot>
              </span>
            </el-tooltip>
          </li>
          <li class="list-item">
            <el-tooltip effect="dark" content="点赞数" placement="top">
              <span>
                <i class="fa fa-star has-text-link"></i>
                <slot name="like-num">{{article.likeNum}}</slot>
              </span>
            </el-tooltip>
          </li>
          <li class="list-item">
            <el-tooltip effect="dark" content="评论数" placement="top">
              <span>
                <i class="fa fa-comment-o has-text-danger"></i>
                <slot name="comment-num">100</slot>
              </span>
            </el-tooltip>
          </li>
          <li class="list-item">
            <el-tooltip effect="dark" content="阅读数" placement="top">
              <span>
                <i class="fa fa-eye has-text-info"></i>
                <slot name="view-num">{{article.viewNum}}</slot>
              </span>
            </el-tooltip>
          </li>
        </ul>
      </div>
      <div class="level">
        <router-link :to="'/showpost/' + article.uuid" class="level-item">READ MORE</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { formatDate } from "plugins/utils.js";
import CardImg from "components/front/common/cardimg/CardImg";

export default {
  props: ["article"],
  name: "PostCard",
  data() {
    return {
      // postTime:""
    };
  },
  methods: {
    showPost() {
      this.$router.push({
        path: `/showpost/${this.article.uuid}`
      });
    }
  },
  computed: {
    postTime() {
      return formatDate(this.article.postTime).toLocaleString();
      // return this.postdata.postTime;
    },
    isExistImg() {
      // return this.article.imgUrl != ""
      return this.article.imgUrl !== "";
    }
  },
  components: {
    CardImg
  }
};
</script>

<style scoped>
.author-title {
  color: gray;
}

.card {
  box-shadow: none;
  border-bottom: 1px dashed #dbdbdb;
  margin-bottom: 5rem;
  /*margin-top: 2rem;*/
}

a {
  color: hsl(0, 0%, 21%);
  transition: 0.3s;
}

a:hover {
  color: #0047ab;
}

.card-content {
  /* .card { */
  /* box-shadow: 0 0.125em 0.25em rgba(10, 10, 10, 0.1); */
  padding-left: 0rem;
  padding-top: 1rem;
}

.title {
  display: inline-block;
  font-size: 1.5rem;
  line-height: 1.4rem;
}

.my-icon {
  display: inline-block;
  margin-right: 0.778rem;
  margin-left: 0.2rem;
}

.list-item span {
  font-size: 0.879rem;
  /* color: #00cfa7; */
  color: #888;
  /* margin-right: 1rem; */
}

.list-item span i {
  padding-right: 0.2rem;
}

.list-item span a {
  color: #888;
}

.content ul {
  margin-left: 0;
  margin-bottom: 1.5rem;
}

.list-item {
  list-style-type: none;
  display: inline-block;
  text-decoration-line: none;
  border-bottom: none;
  padding: 0;
  padding-right: 0.5rem;
}

.level-item {
  color: #34495e;
  font-weight: 700;
}
</style>
