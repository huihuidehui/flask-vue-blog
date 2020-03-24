<template>
  <!-- <div>404页面</div> -->
  <div style="height:100vh" class="page">
    <div class="page-box">
      <p class="page-title">404</p>
      <p>Page Not Found</p>
      <p>You can back to main page.</p>
      <!-- <div class="button"> -->
      <router-link to="/home">
        <button class="button has-text-primary">首页</button>
      </router-link>
      <!-- </div> -->
    </div>
  </div>
</template>

<script>
export default {
  name: "NotFound",
  data() {
    return {};
  }
};
</script>

<style scoped>
.page-title {
  font-size: 9rem;
  font-weight: 100;
}
.page {
  display: flex;
  justify-content: center;
  /* align-items: center; */
  background-color: #fff;
}
.page-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #777;
}
.button {
  margin-top: 1rem;
}
</style>
