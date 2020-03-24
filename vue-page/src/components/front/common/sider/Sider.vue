<template>
  <div>
    <slot></slot>
    <!-- avatars类名用于在导航栏和头像之间留出空隙 -->
    <!-- <slot name="avatars"></slot> -->
    <!-- <slot name="tags-panel"></slot> -->
  </div>
</template>

<script>
// import Avatars from "components/common/avatars/Avatars";
export default {
  name: "Sider",
  data() {
    return {};
  },
  components: {
    // Avatars
  }
};
</script>

<style scoped>
/* <!-- avatars类名用于在导航栏和头像之间留出空隙 --> */
</style>
