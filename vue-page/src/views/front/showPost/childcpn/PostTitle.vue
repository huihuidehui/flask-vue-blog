<template>
  <header class="header">
    <h1 class="title post-title">{{title}}</h1>
    <div class="level">
      <div class="level-left">
        <div class="level-item">
          <ul class="list-inline">
            <li>
              <div class="source">原创</div>
            </li>
            <li>KanHui</li>
            /
            <li>
              <span>
                <i class="fa fa-clock-o"></i>
                {{postTime}}
              </span>
            </li>
            /
            <li>
              <span>
                <i class="fa fa-star-o"></i>
                {{likeNum}}
              </span>
            </li>
            /
            <li>
              <span>
                <i class="fa fa-eye has-text-info"></i>
                {{viewNum}} 次阅读
              </span>
            </li>
          </ul>
        </div>
      </div>
<!--      <div v-if="isDesktop" class="level-right">-->
<!--        <div class="level-item">-->
<!--          <span class="view-num">-->
<!--            <i class="fa fa-eye has-text-info"></i>-->
<!--            {{viewNum}} 次阅读-->
<!--          </span>-->
<!--        </div>-->
<!--      </div>-->
    </div>
  </header>
</template>

<script>
  // import { formatDate } from "plugins/utils.js";
  // import {_isMobile} from "../../../../plugins/utils";

  export default {
    props: ["viewNum", "likeNum", "title", "postTime"],
    name: "PostTitle",
    data() {
      return {};
    },
    // computed: {
      isDesktop() {

        // return _isMobile() == false
      // }
    }
  };
</script>

<style scoped>
  .post-title {
    color: #0047ab;
    margin-top: 0rem;
    margin-bottom: 1rem;
  }

  .view-num {
    font-size: 0.89rem;
    color: #777;
  }

  .list-inline {
    display: inline-block;
    color: #777;
    font-size: 0.89rem;
  }

  .list-inline li {
    list-style: none;
    display: inline-block;
    margin-right: 0.5rem;
    margin-left: 0.5rem;
  }

  .list-inline li:first-child {
    margin-left: 0;
  }

  .source {
    color: red;
    border: 1px solid red;
    padding-left: 5px;
    padding-right: 5px;
    border-radius: 3px;
    font-size: 0.7rem;
  }

  .header {
    /* border-bottom: 1px solid red; */
    border-bottom: 1px solid #ddd;
    padding-bottom: 1.3rem;
    /*margin-top: 1.5rem;*/
    margin-bottom: 1rem;
  }
</style>
