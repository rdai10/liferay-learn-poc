const fs = require('fs');
const sass = require('node-sass');

const clayCss = require('clay-css');

const data = sass.renderSync({
	file: 'source/_static/scss/main.scss',
	includePaths: [clayCss.includePaths]
});

fs.writeFileSync('source/_static/main.css', data.css);
