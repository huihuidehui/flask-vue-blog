<template>
  <div>
    <post-info requestMethod="put"></post-info>
    <!-- <mavon-editor :subfield="false"></mavon-editor> -->
    <!-- </div> -->

    <!-- </div> -->
  </div>
</template>

<script>
import PostInfo from "./PostInfo";
export default {
  name: "CreatePost",
  data() {
    return {};
  },
  components: {
    // "mavon-editor": mavonEditor,
    PostInfo
  }
};
</script>

<style lang="less" scoped>
// .select-info {
//   display: flex;
//   justify-content: space-around;
//   align-items: center;
// }
// .el-input__inner {
//   height: 2px;
//   margin-bottom: 2rem;
// }
// .article-info {
//   margin-top: 2rem;
//   margin-bottom: 2rem;
// }
// .el-input{
// display:inline-block;
// }
// .column{
// display:inline-block
// }
</style>
