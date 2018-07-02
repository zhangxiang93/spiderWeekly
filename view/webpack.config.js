const path = require('path')
const ExtractTextPlugin = require("extract-text-webpack-plugin")

const extractSass = new ExtractTextPlugin({
    filename: "[name].css"
})

module.exports = {
    entry: './src/index.jsx',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, './dist')
    },
    mode: 'development',
    devtool: 'eval-source-map',
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                use: 'babel-loader',
                exclude: /node_moudles/
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            },
            {
                test: /\.scss$/,
                use: extractSass.extract({
                    use: [{
                        loader: "css-loader"
                    }, {
                        loader: "sass-loader"
                    }],
                    // 在开发环境使用 style-loader
                    fallback: "style-loader"
                })
            }
        ]
    },
    plugins: [
        extractSass
    ],
    devServer:{
        host: '65.49.223.6',
        port: 3008,
        compress: true,
        hot: true  
    }
}