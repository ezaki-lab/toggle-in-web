const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  context: path.join(__dirname, 'src'),
  entry: './js/index.jsx',
  output: {
    path: __dirname,
    filename: 'bundle.js',
    publicPath: ''
  },
  module: {
    rules: [
      {
        test: /\.html$/,
        loader: 'html-loader'
      },
      {
        test: /\.css?$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'postcss-loader'
        ]
      },
      {
        test: /\.js$/,
        use: [
          {
            loader: 'esbuild-loader',
            options: {
              loader: 'js'
            }
          }
        ]
      },
      {
        test: /\.jsx$/,
        use: [
          {
            loader: 'esbuild-loader',
            options: {
              loader: 'jsx'
            }
          }
        ]
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      filename: './index.html',
      template: './html/index.html'
    }),
    new MiniCssExtractPlugin({
      filename: './styles.css'
    }),
  ],
  mode: 'production',
  resolve: {
    extensions: ['.js', '.jsx', '.tsx', '.ts']
  },
  // devtool: 'inline-source-map',
  devServer: {
    contentBase: __dirname,
    open: true,
    port: 3000
  }
};
