<template>
  <div class="level">
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
  <!-- </div> -->
</template>

<script>
export default {
  props: ["article"],
  name: "PostInfo",
  data() {
    return {};
  }
};
</script>

<style scoped>
/* .field { */
/* display: inline-block; */
/* } */
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
ul {
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
</style>
