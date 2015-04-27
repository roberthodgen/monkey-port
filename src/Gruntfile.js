module.exports = function(grunt) {
	// Do grunt-related things in here

	// Load Grunt tasks
	grunt.loadNpmTasks('grunt-contrib-clean');
	grunt.loadNpmTasks('grunt-contrib-copy');

	// Project configuration.
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		clean: {
			build: 'static/vendor/*'
		}, copy: {
			ngwp: {
				expand: true,
				cwd: 'src',
				src: '**/*',
				dest: 'dist',
				filter: 'isFile'
			}, bootstrap: {
				expand: true,
				cwd: 'node_modules/bootstrap/dist',
				src: '**/*',
				dest: 'static/vendor/bootstrap',
				filter: 'isFile'
			}, jquery: {
				expand: true,
				cwd: 'node_modules/jquery/dist',
				src: '**/*',
				dest: 'static/vendor/jquery',
				filter: 'isFile'
			}, angular: {
				expand: true,
				cwd: 'node_modules/angular',
				src: '**/*',
				dest: 'static/vendor/angular',
				filter: 'isFile'
			}, angular_route: {
				expand: true,
				cwd: 'node_modules/angular-route',
				src: '**/*',
				dest: 'static/vendor/angular-route',
				filter: 'isFile'
			}, angular_ui_router: {
				expand: true,
				cwd: 'node_modules/angular-ui-router/release',
				src: '**/*',
				dest: 'static/vendor/angular-ui-router',
				filter: 'isFile'
			}, angular_sanitize: {
				expand: true,
				cwd: 'node_modules/angular-sanitize',
				src: '**/*',
				dest: 'static/vendor/angular-sanitize',
				filter: 'isFile'
			}
		}
	});
};