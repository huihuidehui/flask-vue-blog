module.exports = {
  configureWebpack: {
    resolve: {
      alias: {
        components: "@/components",
        content: "components/content",
        common: "components/common",
        assets: "@/assets",
        network: "@/network",
        views: "@/views",
        plugins: "@/plugins",
        store: "@/store",
        router: "@/router"
      }
    },
    externals: {
      'vue': 'Vue',
      'vuex': 'Vuex',
      'vue-router': 'VueRouter',
      'axios': 'axios',
      'element-ui': 'ElEMENT'
    }
  },

  // chainWebpack: config => {
      // .plugin('webpack-bundle-analyzer')
      // .use(require('webpack-bundle-analyzer').BundleAnalyzerPlugin)
// 
    // 压缩代码
    // config.optimization.minimize(true)
  // },

  lintOnSave: false
};




