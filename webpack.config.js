const path = require('path');

module.exports = {
    /* `production` or `development`, but currently there is no diff */
    mode: 'production',


    /* Specify starting point */
    entry: {
        index: path.resolve(__dirname, 'src/App.jsx')
    },

    /* specify output files and where to put them
     * currently outputs all files with their original name */
    output: {
        filename: '[name].js',
        path: path.resolve(__dirname, 'cs499capstone/public/static/js'),
    },


    /* babel-loader will convert *.jsx files to *.js files */
    module: {
        rules: [
            {
                test: /\.m?jsx$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    presets: ['@babel/react'],
                    plugins: [
                        "@babel/plugin-proposal-class-properties"
                    ]
                }
            },
            {
                test: /\.css$/i,
                use: ['style-loader', 'css-loader']
            }
        ]
    },

    /* allow imports inside js without extension. */
    resolve: {
        extensions: ['.js', '.jsx']
    }
};
