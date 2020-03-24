<template>
  <nav class="pagination is-centered is-rounded" role="navigation" aria-label="pagination">
    <router-link :to="'/' +toUrl + '/' + previousPage" class="pagination-previous">上一页</router-link>
    <router-link :to="'/' +toUrl + '/' + nextPage" class="pagination-next">下一页</router-link>

    <!-- <router-link :to="'/' +toUrl + '/' + nextPage" class="pagination-next">下一页</router-link> -->
    <ul class="pagination-list">
      <template v-if="currentPage > 4">
        <!-- 当前页码大于4时，在当前页码前面渲染4个，后面渲染4个 -->
        <li v-for="i in 2" v-bind:key="i">
          <!-- <a v-on:click="jumpPage(i)" class="pagination-link">{{i}}</a> -->
          <router-link :to="'/' +toUrl + '/' + i" class="pagination-link">{{i}}</router-link>
        </li>
        <li>
          <span class="pagination-ellipsis">&hellip;</span>
        </li>
        <li>
          <!-- <a v-on:click="jumpPage(currentPage - 1)" class="pagination-link">{{currentPage-1}}</a> -->
          <router-link :to="'/' +toUrl + '/' + previousPage" class="pagination-link">{{currentPage-1}}</router-link>
        </li>
        <li>
          <!-- <a class="pagination-link is-current">{{currentPage}}</a> -->
          <router-link :to="'/' +toUrl + '/' + currentPage" class="pagination-link is-current">{{currentPage}}</router-link>
        </li>
        <template v-if="totalPage-currentPage>2">
          <li>
            <!-- <a v-on:click="jumpPage(currentPage+1)" class="pagination-link">{{currentPage+1}}</a> -->
            <router-link :to="'/' +toUrl + '/' + nextPage" class="pagination-link">{{nextPage}}</router-link>
          </li>
          <li>
            <span class="pagination-ellipsis">&hellip;</span>
          </li>
          <li>
            <!-- <a v-on:click="jumpPage(totalPage-1)" class="pagination-link">{{totalPage-1}}</a> -->
            <router-link :to="'/' +toUrl + '/' + (totalPage -1)" class="pagination-link">{{totalPage-1}}</router-link>
          </li>
          <li>
            <!-- <a v-on:click="jumpPage(totalPage)" class="pagination-link">{{totalPage}}</a> -->
            <router-link :to="'/' +toUrl + '/' + totalPage" class="pagination-link">{{totalPage}}</router-link>
          </li>
        </template>
        <template v-else>
          <li v-for="i in totalPage-currentPage" v-bind:key="currentPage+i">
            <!-- <a v-on:click="jumpPage(currentPage+i)" class="pagination-link">{{currentPage+i}}</a> -->
            <router-link :to="'/' +toUrl + '/' + nextPage" class="pagination-link">{{nextPage}}</router-link>
          </li>
        </template>
      </template>
      <template v-else>
        <li v-for="i in currentPage" v-bind:key="i">
          <router-link
            :to="'/' +toUrl + '/' + i"
            class="pagination-link"
            v-bind:class="{'is-current':isActive(i)}"
          >{{i}}</router-link>
          <!-- </router-link> -->
        </li>
        <template v-if="totalPage-currentPage>3">
          <li>
            <!-- <router-link to="/home/" +currentPage+1> -->
            <!-- <a v-on:click="jumpPage(currentPage+1)" class="pagination-link">{{currentPage+1}}</a> -->
            <router-link :to="'/' +toUrl + '/' + nextPage" class="pagination-link">{{nextPage}}</router-link>
            <!-- </router-link> -->
          </li>
          <li>
            <span class="pagination-ellipsis">&hellip;</span>
          </li>
          <li>
            <router-link :to="'/' +toUrl + '/' + (totalPage-1)" class="pagination-link">{{totalPage-1}}</router-link>
            <!-- <a v-on:click="jumpPage(totalPage-1)" class="pagination-link">{{totalPage-1}}</a> -->
          </li>
          <li>
            <!-- <a v-on:click="jumpPage(totalPage)" class="pagination-link">{{totalPage}}</a> -->
            <router-link :to="'/' +toUrl + '/' + totalPage" class="pagination-link">{{totalPage}}</router-link>
          </li>
        </template>
        <template v-else>
          <li v-for="i in totalPage-currentPage" v-bind:key="currentPage+i">
            <!-- <a v-on:click="jumpPage(currentPage+1)" class="pagination-link">{{currentPage+i}}</a> -->
            <router-link :to="'/' +toUrl + '/' + (currentPage+i)" class="pagination-link">{{currentPage+i}}</router-link>
          </li>
        </template>
      </template>
    </ul>
  </nav>
</template>

<script>
export default {
  props: ["currentPage", "totalPage","toUrl"],
  name: "Pagination",
  data() {
    return {};
  },
  computed: {
    previousPage() {
      if (this.currentPage > 1) {
        // this.$router.push({ path: `/home/${this.currentPage - 1}` });
        return this.currentPage - 1;
      } else {
        return 1;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPage) {
        return this.currentPage + 1;
      } else {
        return this.totalPage;
      }
    }
  },
  methods: {
    isActive(i) {
      return i == this.currentPage;
    },
    jumpPage(page) {
      // this.$router.push({ path: `/home/${page}` });
      this.$router.push({ path: `/${this.toUrl}/${page}` });
    }
  }
};
</script>

<style scoped>
a {
  color: #777;
}
a:hover {
  color: #c91f37;
  border: 1px solid #c91f37;
}
/* .pagination { */
/* border-bottom: 1px solid #c91f37; */
/* padding-bottom: 4.5rem; */
/* } */
</style>
