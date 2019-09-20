const fs = require('fs');
const path = require('path');
const sass = require('node-sass');

const clayCss = require('clay-css');

fs.readdirSync('source/_static/scss/').forEach(file => {
	const data = sass.renderSync({
		data: fs.readFileSync(path.join('source/_static/scss/', file), 'utf8'),
		includePaths: [clayCss.includePaths]
    });

	fs.writeFileSync('source/_static/main.css', data.css);
});
