module.exports = function(grunt) {
	// Do grunt-related things in here

	// Load Grunt tasks
	grunt.loadNpmTasks('grunt-contrib-clean');
	grunt.loadNpmTasks('grunt-contrib-copy');

	// Project configuration.
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		clean: {
			build: 'src/static/vendor/*'
		}, copy: {
			bootstrap: {
				expand: true,
				cwd: 'node_modules/bootstrap/dist',
				src: '**/*',
				dest: 'src/static/vendor/bootstrap',
				filter: 'isFile'
			}, jquery: {
				expand: true,
				cwd: 'node_modules/jquery/dist',
				src: '**/*',
				dest: 'src/static/vendor/jquery',
				filter: 'isFile'
			}, angular: {
				expand: true,
				cwd: 'node_modules/angular',
				src: '**/*',
				dest: 'src/static/vendor/angular',
				filter: 'isFile'
			}, angular_route: {
				expand: true,
				cwd: 'node_modules/angular-route',
				src: '**/*',
				dest: 'src/static/vendor/angular-route',
				filter: 'isFile'
			}, angular_resource: {
				expand: true,
				cwd: 'node_modules/angular-resource',
				src: '**/*',
				dest: 'src/static/vendor/angular-resource',
				filter: 'isFile'
			}
		}
	});
};