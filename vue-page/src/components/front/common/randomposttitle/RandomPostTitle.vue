<template>
  <li style="list-style-type:none" class="post">
    <p>
      <span>
        <i class="fa fa-hand-o-right title-icon"></i>
      </span>
      <!-- <span class="animated pulse"> -->
      <router-link :to="'/showpost/' + postdata.uuid">
        <slot name="title">{{postdata.title}}</slot>
      </router-link>
      <!-- </span> -->
    </p>
  </li>
</template>

<script>
export default {
  name: "RandomPostTitle",
  data() {
    return {};
  },
  props: ["postdata"],
  methods: {
    addAnimate($event) {
      $event.currentTarget.className = "post animated pulse";
    },
    removeAnimate($event) {
      $event.currentTarget.className = "post";
    }
  }
};
</script>

<style scoped>
.post {
  padding-top: 0.5rem;
  padding-bottom: 0.71rem;
  margin-top: 0.5rem;
  font-size: 0.9rem;
  font-weight: 500;
  border-bottom: solid 1px #eee;
}
.title-icon {
  margin-right: 0.5rem;
}
p {
  -webkit-transition: all 0.15s linear;
  -moz-transition: all 0.15s linear;
  -ms-transition: all 0.15s linear;
  -o-transition: all 0.15s linear;
  transition: all 0.15s linear;
}
p:hover {
  margin-left: 3px;
  color: #0047ab;
}
/* li{ */
/* transition: all 0.3s */
/* } */

/* li { */
/* -webkit-transform: scale(0.9); */
/* -moz-transform: scale(0.9); */
/* -o-transform: scale(0.9); */
/* -webkit-transition-duration: 0.5s; */
/* -moz-transition-duration: 0.5s; */
/* -o/-transition-duration: 0.5s; */
/* } */
/* li:hover { */
/* -webkit-transform: scale(); */
/* -webkit-box-shadow: 0px 0px 30px #ccc; */
/* -moz-transform: scale(1.5); */
/* -moz-box-shadow: 0px 0px 30px #ccc; */
/* -o-transform: scale(1.5); */
/* -o-box-shadow: 0px 0px 30px #ccc; */
/* } */
</style>
