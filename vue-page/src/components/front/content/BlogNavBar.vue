<template>
  <!-- <div class="container column is-four-fifths-widescreen"> -->
  <div class="container column nav is-four-fifths-widescreen">
    <b-navbar :fixed-top="false" class="navbar has-shadow is-spaced">
      <template slot="brand">
        <b-navbar-item tag="router-link" :to="{ path: '/' }">
          <img class="logo" src="~assets/img/logo.png" />
        </b-navbar-item>
      </template>
      <template slot="start">
        <b-navbar-item tag="router-link" to="/home/1">
          <span class="icon has-text-info">
            <i class="fa fa-home"></i>
          </span>
          <span>主页</span>
        </b-navbar-item>
        <!--        <b-navbar-item href="#">-->
        <b-navbar-item tag="router-link" to="/guestbook">
          <span class="icon has-text-link">
            <i class="fa fa-comments-o"></i>
          </span>
          <span>留言</span>
        </b-navbar-item>
        <!--        <b-navbar-item href="#">-->
        <b-navbar-item tag="router-link" to="/archive">
          <span class="icon has-text-link">
            <i class="fa fa-folder"></i>
          </span>
          <span>归档</span>
        </b-navbar-item>
        <b-navbar-dropdown :hoverable="true">
          <template v-slot:label>
            <span class="icon has-text-info">
              <i class="fa fa-tags"></i>
            </span>
            <span>分类</span>
          </template>
          <b-navbar-item
            v-on:click="toCategoryPost(category.id)"
            v-for="category in categories"
            v-bind:key="category.id"
          >{{category.name}}</b-navbar-item>
        </b-navbar-dropdown>

        <b-navbar-item tag="router-link" to="/about">
          <span class="icon has-text-info">
            <i class="fa fa-user"></i>
          </span>
          <span>关于</span>
        </b-navbar-item>
      </template>

      <!-- <template slot="end"> -->
      <!-- <b-navbar-item tag="div"> -->
      <!-- <div class="buttons"> -->
      <!-- <a class="button is-primary"> -->
      <!-- <strong>注册</strong> -->
      <!-- </a> -->
      <!-- <a class="button is-light" v-on:click="login"> -->
      <!-- 登陆 -->
      <!-- </a> -->
      <!-- </div> -->
      <!-- </b-navbar-item> -->
      <!-- </template> -->
    </b-navbar>
  </div>
</template>

<script>
// import NavBar from "components/front/common/navbar/NavBar";
import { request } from "network/request.js";
import { _isMobile } from "../../../plugins/utils";

export default {
  name: "BlogNavBar",
  data() {
    return {
      res: [{ name: name }],
      categories: []
    };
  },
  components: {
    // NavBar
  },
  methods: {
    toCategoryPost(categoryId) {
      this.$router.push({ path: `/category/post/${categoryId}/1` });
    },
    login() {
      this.$router.push({
        path: "/admin/login"
      });
    }
  },
  created() {
    request({
      url: "/categories",
      method: "get"
    })
      .then(res => {
        // console.log(res);
        if (res["res"] == 1) {
          this.categories = res["data"];
        }
      })
      .catch(err => {
        // console.log(res);
      });
  },
  computed: {
    isFixTop() {
      return _isMobile();
    }
  }
};
</script>

<style scoped>
.logo {
  height: 100%;
  border-radius: 100%;
  max-height: 2.6rem;
  /* width:2.6rem; */
  /* color:#8c67ef */
}
.nav{
  padding-top:0px
}
</style>
