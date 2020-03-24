<template>
  <div class="columns is-centered">
    <table>
      <tr>
        <!-- // 插入图片 -->
        <slot name="img"></slot>
      </tr>
      <tr class="img-blank"></tr>
      <tr>
        <div class="has-text-centered">
          <!-- 插入头像地下的文字，作者的名字 -->
          <slot name="text"></slot>
        </div>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: "Avatars",
  data() {
    return {};
  }
};
</script>

<style scoped>
.img-blank {
  height: 1rem;
}
</style>
