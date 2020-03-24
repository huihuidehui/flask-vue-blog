<template>
  <figure class="image is-3by1">
    <img class="post-image" :src="imgUrl" alt="Placeholder image" />
  </figure>
</template>

<script>
export default {
  name: "CardImg",
  props: ["imgUrl"]
};
</script>

<style scoped>
.post-image {
  border-radius: 6px;
}
</style>
