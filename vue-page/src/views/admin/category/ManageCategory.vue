<template>
  <div>
    <div class="category-table">
      <!-- <el-button :plain="true" @click="open2"></el-button> -->

      <p class="title is-size-5">最新分类</p>
      <el-table v-loading="loading" :border="true" :data="categoryData" style="width: 100%">
        <el-table-column type="index" :index="indexMethod"></el-table-column>
        <el-table-column prop="id" label="Id"></el-table-column>
        <el-table-column prop="name" label="名称"></el-table-column>
        <el-table-column prop="articleNum" label="文章数"></el-table-column>
        <!-- <el-table-column prop="postTime" label="发布时间"></el-table-column> -->
        <!-- <el-table-column prop="likeNum" label="点赞数"></el-table-column> -->
        <!-- <el-table-column prop="viewNum" label="阅读数"></el-table-column> -->
        <el-table-column label="操作" width="100">
          <template slot-scope="scope">
            <el-button @click="showCategory(scope.row)" type="text" size="small">查看</el-button>
            <el-button @click="editCategory(scope.row)" type="text" size="small">编辑</el-button>
            <el-button @click="deleteCategory(scope.row)" type="text" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <!-- </div> -->
    </div>
    <!-- <div class="pagination"> -->
    <!-- <el-pagination -->
    <!-- background -->
    <!-- layout="total, sizes, prev, pager, next, jumper" -->
    <!-- :total="totalNum" -->
    <!-- :page-count="totalPage" -->
    <!-- :page-size="pageSize" -->
    <!-- :current-page="currentPage" -->
    <!-- @current-change="handleCurrentChange" -->
    <!-- @size-change="handleSizeChange" -->
    <!-- ></el-pagination> -->
    <!-- </div> -->
  </div>
</template>

<script>
import { adminRequest } from "network/request.js";
import { formatDate } from "plugins/utils.js";
export default {
  name: "ManageCategory",
  data() {
    return {
      //   categoryDataTmp: [],
      categoryData: [],
      loading: true
    };
  },
  methods: {
    showCategory(rowData) {
      // adminRequest()
      // this.$router.push({
      // path:"/category/post"
      // })
      let routeUrl = this.$router.resolve({
        path: `/category/post/${rowData.id}`
      });
      window.open(routeUrl.href, "_blank");
    },
    editCategory(rowData) {
      // console.log(rowData);
      this.$router.push({
        path: "/admin/category/edit",
        query: {
          id: rowData["id"]
        }
      });
    },
    deleteCategory(rowData) {
      // console.log(rowData)
      adminRequest({
        url: "/category",
        params: {
          id: rowData.id
        },
        method: "delete"
      })
        .then(res => {
          if (res["res"] === 1) {
            // 删除成功
            this.$message({
              message: "删除成功",
              type: "success"
            });
            // 删除成功之后重新加载数据
            this.getData();
          } else {
            //   删除失败
            this.$message.error(res["message"]);
          }
          //   console.log(res);
        })
        .catch(err => {
          // 删除失败
          //   console.log(err);
          this.$message.error(res["message"]);
        });
    },
    indexMethod(index) {
      return index + 1;
    },
    getData() {
      adminRequest({
        url: "/categories",
        method: "get"
      })
        .then(res => {
          // 请求成功时
          if (res["res"] == 1) {
            this.categoryData = res["data"];
          }
          this.loading = false;
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
.category-table {
  margin-top: 2rem;
}
.pagination {
  margin-top: 1rem;
  margin-bottom: 1rem;
}
</style>
