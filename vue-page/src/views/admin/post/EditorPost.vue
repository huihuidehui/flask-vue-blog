<template>
  <div>
    <post-info :article="articleData" requestMethod="post"></post-info>
  </div>
</template>

<script>
import PostInfo from "./PostInfo";
import { adminRequest } from "network/request.js";
export default {
  name: "EditorPost",
  data() {
    return {
      articleData: {}
    };
  },
  components: {
    // "mavon-editor": mavonEditor,
    PostInfo
  },
  methods: {
    getData() {
      adminRequest({
        url: "/article",
        params: {
          // uuid: this.$route.params.uuid
          uuid: this.$route.query.uuid
        }
      })
        .then(res => {
          // console.log(res);
          this.articleData = res["data"];
        })
        .catch(err => {
          // console.log(err);
        });
    }
  },
  created() {
    this.getData();
  }
};
</script>

<style scoped>
</style>
