<template>
  <div class="media">
    <div class="media-left">
      <figure class="image is-64x64">
        <!-- <img -->
        <!-- class="img-shadow" -->
        <!-- src="https://madmalls.com/api/medias/uploaded/flask-vuejs-quan-zhan-kai-fa-min-7aeaba5b-60x60.png" -->
        <!-- alt -->
        <!-- /> -->
        <img class="img-shadow" :src="postdata.imgUrl" alt />
      </figure>
    </div>
    <div class="media-content">
      <div>
        <p class="post-title">
          <slot name="title">
            <router-link :to="'/showpost/' + postdata.uuid ">{{postdata.title}}</router-link>
          </slot>
        </p>
      </div>
      <div class="post-info">
        <ul>
          <li class="list-inline-item">
            <slot name="post-time">{{postTime}}</slot>
          </li>
          <li class="list-inline-item">/</li>
          <li class="list-inline-item">
            <span class="view-icon">
              <i class="fa fa-eye"></i>
            </span>
            <slot name="view-num">
              <router-link :to="'/showpost/' + postdata.uuid ">{{postdata.viewNum}}</router-link>
            </slot>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { formatDate } from "plugins/utils.js";
export default {
  props: ["postdata"],
  name: "SiderPost",
  data() {
    return {
      // postTime: ""
    };
  },
  computed: {
    postTime() {
      // console.log("kanhui");
      return formatDate(this.postdata.postTime).toLocaleDateString();
      // return this.postdata.postTime;
    }
  }
};
</script>

<style scoped>
.view-icon {
  margin-right: 0.25rem;
}

.media {
  margin-bottom: 0.8rem;
  border-top: 0px;
}

.list-inline-item {
  display: inline;
  margin-right: 5px;
}
img {
  height: 100%;
  width: auto;
  left: 50%;
  position: relative;
  -webkit-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -moz-transform: translateX(-50%);
}
.img-shadow {
  border-radius: 0.25rem;
  margin-right: 0.5rem;
  background-color: #fff;
  border: 1px solid #ddd;
  padding: 0.15rem;
  box-shadow: 0 5px 20px 0 rgba(0, 0, 0, 0.07);
  /* max-width:2rem; */
  /* overflow: hidden; */
  /* width:10rem; */

  /* width: 100%; */
  /* height: auto; */
  /* top: 50%; */
  /* -webkit-transform: translateY(-50%); */
  /* -ms-transform: translateY(-50%); */
  /* -moz-transform: translateY(-50%); */
  /* position: relative; */
}
.post-info {
  font-size: 0.5rem;
  color: #777;
  margin-top: 1rem;
}
.post-title {
  font-size: 0.9rem;
  line-height: 1.1rem;
  color: #111;
  font-weight: 500;
}
.post-info a {
  color: #777;
}
/* a { */
/* color: #4a4a4a; */
/* transition: all 0.3s; */
/* } */

/* a:hover { */
/* color: #70c02c; */
/* } */
</style>
