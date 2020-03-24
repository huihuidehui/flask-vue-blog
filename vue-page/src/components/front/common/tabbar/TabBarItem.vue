<template>
  <!-- <div> -->
  <!-- <slot></slot> -->
  <!-- </div> -->
  <li :class="{ 'is-active': isActive }">
    <a v-if="isActive" href="#">
      <slot name="tab-text"></slot>
    </a>
    <a v-else href="#">
      <slot name="tab-text"></slot>
    </a>
  </li>
</template>

<script>
export default {
  name: "TabBarItem",
  data() {
    return {};
  },
  props: {
    isActive: {
      type: Boolean,
      default() {
        return false;
      }
    }
  }
};
</script>

<style></style>
