<template>
  <!-- <div>table</div> -->
  <!-- <el-table></el-table> -->
  <div>
    <div class="post-table">
      <p class="title is-size-5">最新文章</p>
      <el-table v-loading="loading" :border="true" :data="articlesData" style="width: 100%">
        <el-table-column type="index" :index="indexMethod"></el-table-column>
        <el-table-column prop="title" label="标题"></el-table-column>
        <el-table-column prop="category" label="分类"></el-table-column>
        <el-table-column prop="postTime" label="发布时间"></el-table-column>
        <el-table-column prop="likeNum" label="点赞数"></el-table-column>
        <el-table-column prop="viewNum" label="阅读数"></el-table-column>
        
      </el-table>
      <!-- <div class="block"> -->
      <!-- <span class="demonstration">页数较少时的效果</span> -->
      <!-- </div> -->
    </div>
    <div class="pagination">
      <el-pagination
        background
        layout="total, sizes, prev, pager, next, jumper"
        :total="totalNum"
        :page-count="totalPage"
        :page-size="pageSize"
        :current-page="currentPage"
        @current-change="handleCurrentChange"
        @size-change="handleSizeChange"
      ></el-pagination>
    </div>
  </div>
</template>

<script>
import { adminRequest } from "network/request.js";
import { formatDate } from "plugins/utils.js";
export default {
  name: "PostTable",
  data() {
    return {
      articlesData: [],
      page: 1,
      currentPage: 1,
      totalPage: 0,
      totalNum: 0,
      loading: true,
      pageSize: 10
    };
  },
  watch: {
    page(newPage) {
      this.getData();
    }
    // pageSize(value)
  },
  created() {
    this.getData();
  },
  methods: {
    indexMethod(index) {
      return index + 1;
    },
    handleSizeChange(value) {
      //   console.log(value);
      this.pageSize = value;
      this.getData();
    },
    getData() {
      adminRequest({
        url: "/articles",
        params: {
          page: this.page,
          size: this.pageSize
        },
        method: "get"
      })
        .then(res => {
          //   格式化数据
          this.articlesData = this.formatPostTime(res["data"]);
          this.totalPage = res["totalPage"];
          this.totalNum = res["totalNum"];
          this.loading = false;
        })
        .catch(err => {
          // console.log(err);
        });
    },
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage;
      this.page = currentPage;
    },
    formatPostTime(articlesData) {
      for (let i = 0; i < articlesData.length; i++) {
        let postTime = articlesData[i].postTime;
        articlesData[i].postTime = formatDate(postTime).toLocaleString();
      }
      return articlesData;
    }
  }
};
</script>

<style scoped>
.post-table {
  margin-top: 2rem;
}
.pagination {
  margin-top: 1rem;
  margin-bottom: 1rem;
}
</style>

