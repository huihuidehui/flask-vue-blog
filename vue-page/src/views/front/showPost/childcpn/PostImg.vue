<template>
  <div class="post-image">
    <figure class="image is-3by1" v-if="isExistImg">
      <img :src="imgUrl" alt="Placeholder image" />
    </figure>
    <div class="post-abstract">
      <span class="sysnopsis">Synopsis:</span>
      <span class="abstract">{{abstract}}</span>
    </div>
    <div class="segmentation">
      <span class="seg">
        <i class="fa fa-paper-plane-o"></i>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  props: ["abstract", "imgUrl"],
  name: "PostImg",
  data() {
    return {};
  },
  computed: {
    isExistImg() {
      return this.imgUrl !== "";
    }
  }
};
</script>

<style scoped>
.seg {
  position: absolute;
  top: -1.8rem;
  width: 4rem;
  height: 4rem;
  background-color: #fff;
  padding-top: 0.63rem;
  border-radius: 100%;
  text-align: center;
  padding-left: 0.7rem;
  padding-bottom: 3rem;
  /* margin-right:3rem; */
}
.fa {
  /* position: absolute; */
  top: -0.06rem;
  width: 2.7rem;
  height: 2.7rem;
  margin-right: 1rem;
  background-color: #eee;
  padding-top: 0.8rem;
  border-radius: 100%;
}
.segmentation {
  height: 5px;
  border-top: 1px dashed #ccc;
  border-bottom: 1px dashed #ccc;
  text-align: center;
  position: relative;
  border-top-width: 1px;
}
.post-abstract {
  margin-bottom: 1.5rem;
}
.image {
  /* border-radius: 6px; */
  box-shadow: 0 5px 20px 0 rgba(0, 0, 0, 0.07);
  margin-bottom: 1.5rem;
}
.image img {
  border-radius: 6px;
}
.post-image {
  margin-top: 1.5rem;
  margin-bottom: 2.5rem;
  /* border-bottom: 10px solid red; */
  /* border-bottom: 1px dashed #dbdbdb; */
  /* border-top: 1px dashed #dbdbdb; */
}
.abstract {
  font-size: 80%;
  /* font-weight: 500; */
  /* color: #70c02c; */
}
.sysnopsis {
  color: #0047ab;
  font-weight: 900;
  margin-right: 0.5rem;
}
</style>
