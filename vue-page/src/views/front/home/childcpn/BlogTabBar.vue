<template>
  <!-- <div>我是tabbar</div> -->
  <!-- <div>
    <tab-bar>
      <tab-bar-item>我是tdddabbar</tab-bar-item>
    </tab-bar>
  </div>-->
  <tab-bar class="blog-tab-bar">
    <template v-slot:items>
      <tab-bar-item>
        <template v-slot:tab-text>文章</template>
      </tab-bar-item>
      <tab-bar-item>
        <template v-slot:tab-text>文章</template>
      </tab-bar-item>
      <tab-bar-item :isActive="true">
        <template v-slot:tab-text>文章</template>
      </tab-bar-item>
    </template>
  </tab-bar>
</template>

<script>
import TabBar from "components/common/tabbar/TabBar";
import TabBarItem from "components/common/tabbar/TabBarItem";
export default {
  name: "BlogTabBar",
  components: {
    TabBar,
    TabBarItem
  }
};
</script>

<style>
/* 与导航栏留出一定空隙，大小跟avatars与导航栏的空隙一致 */
.blog-tab-bar {
  padding-top: 1.8rem;
  padding-bottom: 0.5rem;
}
</style>
