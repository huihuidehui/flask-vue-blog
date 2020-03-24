<template>
  <!-- <div> -->
  <category-info :method="requestMethod"></category-info>
  <!-- </el-form> -->
</template>

<script>
import CategoryInfo from "./CategoryInfo";
export default {
  name: "CreateCategory",
  data() {
    return {
      //   form: {
      // name: ""
      //   }
      requestMethod: "put"
    };
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
