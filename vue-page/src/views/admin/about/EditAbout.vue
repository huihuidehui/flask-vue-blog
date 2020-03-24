<template>
  <el-form ref="form" size="mini" :model="this.aboutData" label-width="80px">
    <!-- <post-info :article="articleData" requestMethod="post"></post-info> -->
    <el-form-item label="简介内容:">
      <mavon-editor v-model="aboutData.content"></mavon-editor>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit" :plain="true">提交</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
// import PostInfo from "./PostInfo";
import { adminRequest } from "network/request.js";
import { mavonEditor } from "mavon-editor";
import "mavon-editor/dist/css/index.css";
export default {
  name: "EditorAbout",
  data() {
    return {
      aboutData: {
        content: ""
      }
    };
  },
  components: {
    "mavon-editor": mavonEditor
    // PostInfo
  },
  methods: {
    onSubmit() {
      adminRequest({
        url: "/about",
        method: "post",
        data: this.aboutData
      })
        .then(res => {
        //   console.log(res);
          if (res["res"] === 1) {
            this.$message({
              message: "修改成功",
              type: "success"
            });
          } else {
            this.$message.error(res.message);
          }
        })
        .catch(err => {
          this.$message.error(err["message"]);
        });
    },
    getData() {
      adminRequest({
        url: "/about"
        // params: {
        // uuid: this.$route.params.uuid
        //   uuid: this.$route.query.uuid
        // }
      })
        .then(res => {
        //   console.log(res.data.content);
          this.aboutData.content = res.data.content;
        })
        .catch(err => {
        //   console.log(err);
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