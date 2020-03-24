import Vue from "vue";
import VueRouter from "vue-router";
import front from "./modules/front";
import admin from "./modules/admin";
import store from "store/index.js";
const NotFound = () => import("views/notfound/NotFound.vue");

Vue.use(VueRouter);
let routes = [
  ...front,
  ...admin,
  {
    name: '404',
    path: '/404',
    component: NotFound
  },
  {
    path: '*',    // 此处需特别注意至于最底部
    redirect: '/404'
  }
]

// let routes;
const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes: routes,
  // 切换路由后页面返回顶部
  scrollBehavior(to, from, savedPosition) {
    // return 期望滚动到哪个的位置
    if (savedPosition) {
      return savedPosition
    } else {
      return { x: 0, y: 0 }
    }
  }
})

router.beforeEach((to, from, next) => {
  if (to.meta.hasOwnProperty("requireAuth")) {
    // 请求要求权限的路由，判断是否有权限
    if (store.state.token !== "") {
      // token值不为空时
      next()
    } else {
      // console.log("没有权限")
      router.push({ path: "/admin/login" })
    }
  }
  next()
})

export default router;
