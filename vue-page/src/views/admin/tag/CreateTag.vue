<template>
  <!-- <div> -->
  <tag-info :method="requestMethod"></tag-info>
  <!-- </el-form> -->
</template>

<script>
import TagInfo from "./TagInfo";
export default {
  name: "CreateTag",
  data() {
    return {
      requestMethod: "put"
    };
  },
  components: {
    TagInfo
  }
};
</script>

<style scoped>
</style>