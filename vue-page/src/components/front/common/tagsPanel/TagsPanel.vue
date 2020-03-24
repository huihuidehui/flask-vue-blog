<template>
  <!-- <div class="container"> -->
  <div class="columns is-multiline">
    <!-- <div class="column tag-panel-title"> -->
      <!-- <span class="title is-6">标签云</span> -->
    <!-- </div> -->
    <div class="tags are-medium">
      <slot name="tag-item"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "TagsPanel",
  data() {
    return {};
  }
};
</script>

<style scoped>
.tag-panel-title {
  display: flex;
  justify-content: center;
}
</style>
