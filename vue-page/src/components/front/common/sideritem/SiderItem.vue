<template>
  <div class="side-item">
    <div class="head">
      <div class="head-title">
        <slot name="title"></slot>
      </div>
    </div>
    <div>
      <slot name="items"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "SiderItem",
  data() {
    return {};
  },
  components: {}
};
</script>

<style scoped>
.head-title {
  position: relative;
  color: #0047ab;
  top: 1px;
  display: inline-block;
  margin: 0px;
  border-color: #0047ab;
  padding-bottom: 0.7rem;
  border-bottom: 1px solid #555;
  border-color: #0047ab;
  font-size: 1.15rem;
  font-weight: 500;
}
.head {
  border-bottom: 1px dotted #ccc;
  margin-bottom: 1.5rem;
  /*margin-top: 1.5rem;*/
}
</style>
