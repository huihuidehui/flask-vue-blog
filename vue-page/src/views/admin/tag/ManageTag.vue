<template>
  <div>
    <div class="tag-table">
      <!-- <el-button :plain="true" @click="open2"></el-button> -->

      <p class="title is-size-5">最新标签</p>
      <el-table v-loading="loading" :border="true" :data="tagData" style="width: 100%">
        <el-table-column type="index" :index="indexMethod"></el-table-column>
        <el-table-column prop="id" label="Id"></el-table-column>
        <el-table-column prop="name" label="名称"></el-table-column>
        <el-table-column prop="articleNum" label="文章数"></el-table-column>
        <!-- <el-table-column prop="postTime" label="发布时间"></el-table-column> -->
        <!-- <el-table-column prop="likeNum" label="点赞数"></el-table-column> -->
        <!-- <el-table-column prop="viewNum" label="阅读数"></el-table-column> -->
        <el-table-column label="操作" width="100">
          <template slot-scope="scope">
            <el-button @click="showtag(scope.row)" type="text" size="small">查看</el-button>
            <el-button @click="edittag(scope.row)" type="text" size="small">编辑</el-button>
            <el-button @click="deletetag(scope.row)" type="text" size="small">删除</el-button>
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
  name: "Managetag",
  data() {
    return {
      //   tagDataTmp: [],
      tagData: [],
      loading: true
    };
  },
  methods: {
    showtag(rowData) {
      // adminRequest()
      // this.$router.push({
      // path:"/tag/post"
      // })
      let routeUrl = this.$router.resolve({
        path: `/tag/post/${rowData.tagId}`
      });
      window.open(routeUrl.href, "_blank");
    },
    edittag(rowData) {
      this.$router.push({
        path: "/admin/tag/edit",
        query: {
          id: rowData["tagId"]
        }
      });
    },
    deletetag(rowData) {
      adminRequest({
        url: "/tag",
        params: {
          id: rowData.tagId
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
        })
        .catch(err => {
          // 删除失败
          this.$message.error(res["message"]);
        });
    },
    indexMethod(index) {
      return index + 1;
    },
    getData() {
      adminRequest({
        url: "/tags",
        method: "get"
      })
        .then(res => {
          // 请求成功时
          if (res["res"] == 1) {
            this.tagData = res["data"];
          }
          this.loading = false;
        })
        .catch(err => {
        });
    }
  },
  created() {
    this.getData();
  }
};
</script>

<style scoped>
.tag-table {
  margin-top: 2rem;
}
.pagination {
  margin-top: 1rem;
  margin-bottom: 1rem;
}
</style>
