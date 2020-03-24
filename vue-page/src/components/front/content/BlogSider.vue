<template>
  <sider class="side" id="sider">
    <sider-item class="item">
      <template v-slot:title>热门文章</template>
      <template v-slot:items>
        <ul>
          <sider-post v-for="post in popularPostData" :key="post.uuid" v-bind:postdata="post"></sider-post>
          <!-- <sider-post></sider-post> -->
          <!-- <sider-post></sider-post> -->
          <!-- <sider-post></sider-post> -->
        </ul>
      </template>
    </sider-item>
    <sider-item class="item">
      <template v-slot:title>最新文章</template>
      <template v-slot:items>
        <ul>
          <random-post-title v-for="post in newPostData" :key="post.uuid" v-bind:postdata="post"></random-post-title>
          <!-- <random-post-title></random-post-title> -->
          <!-- <random-post-title></random-post-title> -->
          <!-- <random-post-title></random-post-title> -->
        </ul>
      </template>
    </sider-item>
    <sider-item class="item">
      <template v-slot:title>标签云</template>
      <template v-slot:items>
        <div class="tags">
          <router-link :to="'/tag/' +  'post/' +tag.tagId +'/' + 1" v-for="tag in tagData" :key="tag.tagId">
            <simple-tag>{{tag.name}}</simple-tag>
          </router-link>
        </div>
        <!-- </tags-panel> -->
      </template>
    </sider-item>
  </sider>
</template>

<script>
import Sider from "components/front/common/sider/Sider";
import SiderItem from "components/front/common/sideritem/SiderItem";
import SiderPost from "components/front/common/siderpost/SiderPost";
import RandomPostTitle from "components/front/common/randomposttitle/RandomPostTitle";
import SimpleTag from "components/front/common/tagsPanel/SimpleTag";
// import TagsPanel from "components/front/common/tagsPanel/TagsPanel";
import { request } from "network/request.js";
export default {
  name: "BlogSider",
  data() {
    return {
      popularPostData: [],
      newPostData: [],
      tagData: []
    };
  },
  components: {
    SimpleTag,
    Sider,
    SiderItem,
    SiderPost,
    RandomPostTitle
  },
  created() {
    this.getPopularPosts();
  },
  methods: {
    getPopularPosts() {
      request({
        url: "/popularposts",
        method: "get",
        params: {
          count: 4
        }
      })
        .then(res => {
          if (res["res"] == 1) {
            this.popularPostData = res["data"];
          }
        })
        .catch(err => {
          // console.log(err);
        });
      request({
        url: "/newposts",
        method: "get",
        params: {
          count: 4
        }
      })
        .then(res => {
          if (res["res"] == 1) {
            this.newPostData = res["data"];
          }
          // console.log(res);
        })
        .catch(err => {
          // console.log(err);
        });
      request({
        url: "/tags",
        method: "get"
      })
        .then(res => {
          if (res["res"] == 1) {
            this.tagData = res["data"];
          }
        })
        .catch(err => {
          // console.log(err);
        });
    }
  }
};
</script>

<style scoped>
 .item {
 margin-bottom: 1.5rem;
 }
</style>
