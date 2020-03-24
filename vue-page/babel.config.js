module.exports = {
  presets: [
    ['@babel/preset-env', { 'modules': false }]
  ],
  'plugins': [
    [
      'component',
      {
        'libraryName': 'element-ui',
        'styleLibraryName': 'theme-chalk'
      },
    ],
    [
      "prismjs",
      {
        "languages": ["html", "css", "javascript", "php", "dart", "bash", "python", "nginx", "sql"],

        "plugins": ["toolbar",
          "show-language",
          "copy-to-clipboard",
          "line-numbers"],//使用了行号还可以添加其他插件，具体去官网看看吧

        "theme": "twilight",
        "css": false
      }
    ]
  ]
}