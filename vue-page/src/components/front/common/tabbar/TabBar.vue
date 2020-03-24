<template>
  <!-- <div> -->
  <!-- <slot></slot> -->
  <!-- </div> -->
  <nav class="breadcrumb has-arrow-separator">
    <ul>
      <slot name="items"></slot>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "TabBar",
  data() {
    return {};
  }
};
</script>

<style scoped></style>
