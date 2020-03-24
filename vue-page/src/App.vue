<template>
  <div id="app">
    <template v-if="isAdmin">
      <router-view name="admin"></router-view>
    </template>
    <div v-if="isFront">
      <el-backtop :bottom="50">
        <i class="el-icon-caret-top"></i>
      </el-backtop>
      <blog-nav-bar></blog-nav-bar>
      <!--    <div class="container">-->
      <div class="container column is-four-fifths-widescreen section">
        <router-view></router-view>
      </div>

      <blog-footer></blog-footer>
    </div>
  </div>
</template>

<script>
import BlogNavBar from "components/front/content/BlogNavBar";
import BlogFooter from "components/front/content/BlogFooter";

export default {
  name: "App",
  data() {
    return {
      isFront: false,
      isAdmin: false,
      userList: [{ name: "kanhui" }, { name: "kanhiuhui" }, { name: "test" }]
    };
  },
  components: {
    BlogNavBar,
    BlogFooter
  },
  watch: {
    $route() {
      this.isFront = this.$route.fullPath.indexOf("admin") == -1;
      this.isAdmin = !this.isFront;
    }
  }
};
</script>

<style lang="scss">
/*@import "~bulma/sass/utilities/_all";*/

.blog-aside {
  height: 100vh;
}
</style>
