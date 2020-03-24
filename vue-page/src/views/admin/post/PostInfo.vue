<template>
  <div>
    <!-- 文章信息表单 -->
    <el-form ref="form" size="mini" :model="form" label-width="80px">
      <el-form-item label="文章标题">
        <el-input v-model="form.title"></el-input>
      </el-form-item>
      <el-form-item label="分类">
        <el-select v-model="form.category" placeholder="请选择文章分类">
          <el-option
            v-for="item in categoryList"
            :key="item.id"
            :label="item.name"
            :value="item.name"
          ></el-option>
        </el-select>
      </el-form-item>

      <el-form-item label="阅读数">
        <el-input-number v-model="form.viewNum" :min="0" label="阅读数"></el-input-number>
      </el-form-item>
      <el-form-item label="点赞数">
        <el-input-number v-model="form.likeNum" :min="0" label="点赞数"></el-input-number>
      </el-form-item>

      <el-form-item label="标签">
        <el-select v-model="form.tags" multiple placeholder="请选择文章标签">
          <el-option v-for="item in tagList" :key="item.id" :label="item.name" :value="item.name"></el-option>
        </el-select>
      </el-form-item>

      <el-form-item label="发布时间">
        <!-- <el-col :span="11"> -->

    <el-date-picker
      v-model="form.date" style:="width:100%"
      type="datetime"
      placeholder="选择日期时间">
    </el-date-picker>


          <!-- <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker> -->
        <!-- </el-col> -->
        <!-- <el-col class="line" :span="2">-</el-col> -->
        <!-- <el-col :span="11"> -->
          <!-- <el-time-picker placeholder="选择时间" v-model="form.date2" style="width: 100%;"></el-time-picker> -->
        <!-- </el-col> -->
      </el-form-item>
      <el-form-item label="文章简介">
        <el-input type="textarea" v-model="form.desc"></el-input>
      </el-form-item>

      <el-form-item label="Url">
        <el-input v-model="form.coverImgUrl" placeholder="文章封面图片url"></el-input>
      </el-form-item>
      <el-form-item label="文章正文">
        <mavon-editor v-model="form.content" @save="saveContent"></mavon-editor>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit" :plain="true">提交</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { mavonEditor } from "mavon-editor";
import "mavon-editor/dist/css/index.css";
import { adminRequest } from "network/request.js";
import { formatDate } from "plugins/utils.js";
export default {
  props: ["article", "requestMethod"],
  name: "PostInfo",
  data() {
    return {
      categoryList: [],
      //   网络请求得到的标签信息
      tagList: [],
      form: {
        title: "",
        category: "",
        date: "",
        // date2: "",
        tags: [],
        desc: "",
        content: "",
        coverImgUrl: "",
        viewNum: 0,
        likeNum: 0
      }
    };
  },
  computed: {},
  components: {
    "mavon-editor": mavonEditor
  },
  watch: {
    article(value) {
      // console.log(value);
      // 传入已有的文章进行修改
      this.fillData();
    }
  },
  created() {
    this.getCategoryData();
    this.getTagData();
  },
  methods: {
    fillData() {
      this.form.title = this.article.title;
      this.form.content = this.article.content;
      this.form.desc = this.article.abstract;
      this.form.likeNum = this.article.likeNum;
      this.form.viewNum = this.article.viewNum;
      this.form.coverImgUrl = this.article.imgUrl;
      this.form.category = this.article.category;
      this.form.tags = this.article.tags;
      this.form.date = this.article.postTime;
      // this.form.date1 = this.article.postTime;
    },
    saveContent(value, renderValue) {
    },
    onSubmit() {
      // 处理时间
      let newPostTime = formatDate(this.form.date).getTime() / 1000;
      // 要发送到服务器的数据
      let sentData = {
        title: this.form.title,
        content: this.form.content,
        abstract: this.form.desc,
        category: this.form.category,
        tags: this.form.tags,
        // likeNum
        postTime: newPostTime,
        coverImgUrl: this.form.coverImgUrl,
        viewNum: this.form.viewNum,
        likeNum: this.form.likeNum
      };

      // 判断如果是修改文章则填入文章id
      if (this.requestMethod === "post") {
        sentData["id"] = this.article.id;
      }
      // console.log(sentData)
      adminRequest({
        url: "/article",
        method: this.requestMethod,
        data: sentData
      })
        .then(res => {
          if (res["res"] == 1) {
            this.$message({
              message: res["message"],
              type: "success"
            });
          } else {
            this.$message.error(res["message"]);
          }
        })
        .catch(err => {
          this.$message.error(err["message"]);
          // console.log(err);
          //   if(err["message"])
        });
    },
    getTagData() {
      adminRequest({
        url: "/tags",
        method: "get"
      })
        .then(res => {
          this.tagList = res["data"];
        })
        .catch(err => {});
    },
    getCategoryData() {
      adminRequest({
        url: "/categories",
        method: "get"
      })
        .then(res => {
          this.categoryList = res["data"];
        })
        .catch(err => {});
    }
  }
};
</script>

<style scoped>
</style>
