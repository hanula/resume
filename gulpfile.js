var gulp = require('gulp'),
	install = require("gulp-install");
gulp.task('default',function() {
	gulp.src(['./requirements.txt'])
		.pipe(install());
});
