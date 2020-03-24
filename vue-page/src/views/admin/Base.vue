<template>
  <el-container style="height: 100vh">
    <app-aside></app-aside>
    <el-container>
      <app-header></app-header>
      <el-main>
        <router-view></router-view>
        <!-- <post-info requestMethod="put"></post-info> -->
        <!-- <mavon-editor :subfield="false"></mavon-editor> -->
        <!-- </div> -->

        <!-- </div> -->
      </el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </el-container>
</template>

<script>
import Aside from "components/admin/content/Aside";
import Header from "components/admin/content/Header";
export default {
  name: "Base",
  data() {
    return {};
  },
  components: {
    "app-aside": Aside,
    "app-header": Header
    // "mavon-editor": mavonEditor,
    // PostInfo
  }
};
</script>

<style scoped>
.el-main {
  background-color: #f3f3f4;
}
.el-footer{
  background-color: #f3f3f4;
}
</style>
