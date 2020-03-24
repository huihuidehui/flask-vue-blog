import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
// 引入bulma样式库
// import "bulma/css/bulma.css";
import "./assets/css/base.css";
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import MetaInfo from 'vue-meta-info'
import { Navbar } from 'buefy'
Vue.use(Navbar)
Vue.use(MetaInfo)
Vue.use(ElementUI)
Vue.config.productionTip = false;




new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
