<template>
  <category-info :category="categoryData" :method="requestMethod"></category-info>
</template>

<script>
import CategoryInfo from "./CategoryInfo";
import { adminRequest, request } from "network/request.js";
export default {
  name: "EditCategory",
  data() {
    return {
      categoryData: {},
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
        url: "/category",
        params: {
          name: "kanhui",
          id: this.$route.query.id
        },
        method: "get"
      })
        .then(res => {
          // console.log(res);
          if (res["res"] === 1) {
            this.categoryData = res["data"];
          }
        })
        .catch(err => {
          // console.log(err);
        });
    }
  },
  components: {
    CategoryInfo
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
