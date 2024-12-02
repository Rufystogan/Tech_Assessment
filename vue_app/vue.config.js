// vue.config.js
module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'https://assessment.takafulbrunei.com',
        changeOrigin: true,
        pathRewrite: {
          '^/api': '', // Optional: Rewrite the URL path (if needed)
        },
      },
    },
  },
};
