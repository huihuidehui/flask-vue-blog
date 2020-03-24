<template>
  <article>
    <slot name="PostTitle"></slot>
    <slot name="PostImg"></slot>
    <slot name="PostContent"></slot>
    <slot name="PostProperty"></slot>
    <slot name="PostStatement"></slot>
    <slot name="PostInfo"></slot>
  </article>
</template>

<script>
export default {
  name: "Post",
  data() {
    return {};
  }
};
</script>

<style scoped>
</style>
