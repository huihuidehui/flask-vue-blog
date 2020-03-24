<template>
  <!-- <div>table</div> -->
  <!-- <el-table></el-table> -->
  <div>
    <div class="post-table">
      <!-- <el-button :plain="true" @click="open2"></el-button> -->

      <p class="title is-size-5">最新文章</p>
      <el-table v-loading="loading" :border="true" :data="articlesData" style="width: 100%">
        <el-table-column type="index" :index="indexMethod"></el-table-column>
        <el-table-column prop="title" label="标题"></el-table-column>
        <el-table-column prop="category" label="分类"></el-table-column>
        <el-table-column prop="postTime" label="发布时间"></el-table-column>
        <el-table-column prop="likeNum" label="点赞数"></el-table-column>
        <el-table-column prop="viewNum" label="阅读数"></el-table-column>
        <el-table-column label="操作" width="100">
          <template slot-scope="scope">
            <el-button @click="showPost(scope.row)" type="text" size="small">查看</el-button>
            <el-button @click="editPost(scope.row)" type="text" size="small">编辑</el-button>
            <el-button @click="deletePost(scope.row)" type="text" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
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
  name: "ManagePost",
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
    showPost(rowData) {
      //   console.log(row);
      let routeUrl = this.$router.resolve({
        path: `/showpost/${rowData.uuid}`
      });
      window.open(routeUrl.href, "_blank");
    },
    editPost(rowData) {
      // console.log(rowData)
      this.$router.push({
        // path: `/admin/article/edit/${rowData.uuid}`
        path: "/admin/article/edit",
        query: {
          uuid: rowData.uuid
        }
      });
    },
    deletePost(rowData) {
      adminRequest({
        url: "/article",
        method: "delete",
        params: {
          uuid: rowData.uuid
        }
      })
        .then(res => {
          if (res["res"] === 1) {
            this.$message({
              message: "删除成功",
              type: "success"
            });
            // 重新获取数据并刷新页面
            this.getData();
          } else {
            this.$message.error(res["message"]);
          }
        })
        .catch(err => {
          this.$message.error(res["message"]);
          //   console.log(err);
        });
    },
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

