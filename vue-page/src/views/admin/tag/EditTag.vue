<template>
  <tag-info :tag="tagData" :method="requestMethod"></tag-info>
</template>

<script>
import TagInfo from "./TagInfo";
import { adminRequest, request } from "network/request.js";
export default {
  name: "EditTag",
  data() {
    return {
      tagData: {},
      requestMethod: "post"
    };
  },
  created() {
    this.getData();
  },
  methods: {
    getData() {
      //   adminRequest({
      adminRequest({
        url: "/tag",
        params: {
          name: "kanhui",
          id: this.$route.query.id
        },
        method: "get"
      })
        .then(res => {
          if (res["res"] === 1) {
            this.tagData = res["data"];
          }
        })
        .catch(err => {
        });
    }
  },
  components: {
    TagInfo
  }
  //   methods: {
  //   onSubmit(){
  //   }
  //   }
};
</script>

<style scoped>
/* .el-form { */
/* display: flex; */
/* align-items: center; */
/* } */
</style>