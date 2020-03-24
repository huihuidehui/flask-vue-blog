<template>
  <!-- <el-container class="home-container"> -->
  <!-- <app-aside></app-aside> -->
  <!-- <el-container> -->
  <!-- <app-header></app-header> -->
  <!-- <el-main> -->
  <div>
    <icon-card></icon-card>
    <post-table></post-table>
  </div>
  <!-- </el-main> -->
  <!-- <el-footer>Footer</el-footer> -->
  <!-- </el-container> -->
  <!-- </el-container> -->
</template>

<script>
// import Aside from "components/admin/content/Aside";
// import Header from "components/admin/content/Header";
import IconCard from "./childcpn/IconCard";
import PostTable from "./childcpn/PostTable";
export default {
  name: "Index",
  data() {
    return {};
  },
  components: {
    // "app-aside": Aside,
    // "app-header": Header,
    IconCard,
    PostTable
  }
};
</script>

<style lang="less" scoped>
// .el-header {
// background-color: #f3f3f3;
// }
// .el-

// .home-container {
  // height: 100vh;
// }
// .el-main {
  // background-color: #f0f2f5;
// }
// .el-footer {
  // background: #f0f2f5;
// }
</style>
