import axios from "axios";
import store from "store/index.js";
import router from "router/index.js";
import { Loading } from "element-ui"

let loading;
//内存中正在请求的数量
let loadingNum = 0;
function startLoading() {
  if (loadingNum == 0) {
    loading = Loading.service({
      lock: true,
      text: '拼命加载中...',
      background: 'rgba(255,255,255,0.5)',
    })
  }
  //请求数量加1
  loadingNum++;
}
function endLoading() {
  //请求数量减1
  loadingNum--
  if (loadingNum <= 0) {
    loading.close()
  }
}

export function request(config) {
  // 1.创建axios的实例
  const instance = axios.create({
    baseURL: "http://127.0.0.1:5000",
    timeout: 5000
  });
  //   axios的拦截器
  // 请求拦截的作用
  instance.interceptors.request.use(
    config => {
      startLoading();
      return config;
    },
    err => {
      startLoading();
      // console.log(err);
    }
  );
  //   响应拦截
  instance.interceptors.response.use(
    res => {
      // console.log("successful")
      endLoading();
      return res.data;
    },
    err => {
      endLoading();
      if (err.response.status == 401) {
        return Promise.reject(err.response.data)
      }
      return Promise.reject(error.response.data) // 返回接口返回的错误信息
    }
    // }
  );
  //   发送真正的请求
  return instance(config);
}

export function adminRequest(config) {
  // 1.创建axios的实例
  const instance = axios.create({
    baseURL: "http://127.0.0.1:5000",
    timeout: 5000
  });
  //   axios的拦截器
  // 请求拦截的作用
  instance.interceptors.request.use(
    config => {
      startLoading();
      // 给每个请求添加token
      if (store.state.token !== "") {
        config.headers.Authorization = "Bearer " + store.state.token
      }
      return config;
    },
    err => {
      // console.log(err);
    }
  );
  //   响应拦截
  instance.interceptors.response.use(
    res => {
      endLoading();
      return res.data;
    },
    err => {
      endLoading();
      if (err.response.status == 401) {
        // 跳转到登陆页面
        router.push({ path: "/admin/login" });
        return Promise.reject(err.response.data)
      }
      return Promise.reject(error.response.data) // 返回接口返回的错误信息
    }
    // }
  );
  //   发送真正的请求
  return instance(config);
}