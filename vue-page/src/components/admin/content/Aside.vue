<template>
  <el-aside width="auto">
    <el-menu
      :default-active="activeTab"
      class="el-menu-vertical-demo"
      background-color="#2c3b4e"
      text-color="#fff"
      active-text-color="#ffd04b"
      :collapse="isExpansion"
      router
    >
      <el-menu-item index="/admin/index" :route="{path:'/admin/index'}">
        <i class="el-icon-location"></i>
        <span>首页</span>
      </el-menu-item>
      <!-- <el-menu-item index="/admin/category"> -->
      <!-- <i class="el-icon-menu"></i> -->
      <!-- <span slot="title">分类</span> -->
      <!-- </el-menu-item> -->
      <el-submenu index="3">
        <template v-slot:title>
          <i class="el-icon-document"></i>
          <span slot="title">文章</span>
        </template>
        <el-menu-item index="/admin/article/create" :route="{path:'/admin/article/create'}">
          <i class="el-icon-document"></i>
          <span slot="title">写文章</span>
        </el-menu-item>
        <el-menu-item
          :disabled="isInEditPage"
          index="/admin/article/edit"
          :route="{path:'/admin/article/edit'}"
        >
          <i class="el-icon-document"></i>
          <span slot="title">编辑文章</span>
        </el-menu-item>
        <el-menu-item index="/admin/article/managepost" :route="{path:'/admin/article/managepost'}">
          <i class="el-icon-document"></i>
          <span slot="title">管理文章</span>
        </el-menu-item>
      </el-submenu>

      <el-submenu index="3">
        <template v-slot:title>
          <i class="el-icon-document"></i>
          <span slot="title">分类</span>
        </template>
        <el-menu-item index="/admin/category/create" :route="{path:'/admin/category/create'}">
          <i class="el-icon-document"></i>
          <span slot="title">创建分类</span>
        </el-menu-item>
        <el-menu-item index="/admin/category/manage" :route="{path:'/admin/category/manage'}">
          <i class="el-icon-document"></i>
          <span slot="title">管理分类</span>
        </el-menu-item>
      </el-submenu>

      <el-submenu index="4">
        <template v-slot:title>
          <i class="el-icon-document"></i>
          <span slot="title">标签</span>
        </template>
        <el-menu-item index="/admin/tag/create" :route="{path:'/admin/tag/create'}">
          <i class="el-icon-document"></i>
          <span slot="title">创建标签</span>
        </el-menu-item>
        <el-menu-item index="/admin/tag/manage" :route="{path:'/admin/tag/manage'}">
          <i class="el-icon-document"></i>
          <span slot="title">管理标签</span>
        </el-menu-item>
      </el-submenu>

      <!-- <el-menu-item index="7"> -->
      <!-- <i class="el-icon-setting"></i> -->
      <!-- <span slot="title">标签</span> -->
      <!-- </el-menu-item> -->
      <!-- 多级菜单 -->
      <el-submenu index="8">
        <template v-slot:title>
          <i class="el-icon-setting"></i>
          <span>其他</span>
        </template>
        <el-menu-item index="9">
          <i class="el-icon-setting"></i>
          <span slot="title">网站配置</span>
        </el-menu-item>
        <el-menu-item index="/admin/about" :route="{path:'/admin/about'}">
          <i class="el-icon-setting"></i>
          <span slot="title">个人简介</span>
        </el-menu-item>
      </el-submenu>
      <el-menu-item v-on:click="isCollapse">
        <i class="el-icon-menu"></i>
        <span>收起</span>
      </el-menu-item>
    </el-menu>
  </el-aside>
</template>

<script>
export default {
  name: "Aside",
  data() {
    return {
      isExpansion: false,
      asideWidth: "200px"
    };
  },
  methods: {
    isCollapse() {
      this.isExpansion = !this.isExpansion;
      //   this.
    }
  },
  computed: {
    activeTab() {
      return this.$route.path;
    },
    // 用于在非编辑页面禁用编辑文章选项卡
    isInEditPage() {
      return this.$route.path !== "/admin/article/edit";
    }
  }
};
</script>

<style scoped>
.el-aside {
  background-color: #2c3b4e;
}
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
span {
  color: #fff;
}
</style>
