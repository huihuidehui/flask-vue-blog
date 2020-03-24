<template>
  <a class="column tag auto blog-tag">
    <slot></slot>
  </a>
</template>

<script>
export default {
  name: "SimpleTag",
  data() {
    return {};
  }
};
</script>
<style scoped>
.blog-tag {
  /* padding: 10px; */
  /* margin: 5px; */
  /* margin-left: 0px; */
  height: 20%;
  /* max-height: 30%; */
  border: 1px solid #eee;
  background-color: transparent;
  font-size: 0.77rem;
  padding-left: 0.5rem;
  padding-right: 0.5rem;
  line-height: 0.6rem;
}
/* a { */
/* text-decoration-line: none; */
/* } */
a {
  transition: all 0.3s;
}
a:hover {
  text-decoration-line: none;
  color: #111;
  background-color: #0047ab;
}
</style>
