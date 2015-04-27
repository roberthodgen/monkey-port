(function() {

	var app = angular.module('mp', [
		'ngRoute',

		'mp.createPoll'
	]);

	// Configure the $routeProvider's routes
	app.config(['$routeProvider', function($routeProvider) {

		// Route handlers
		$routeProvider.when('/', {
			templateUrl: '/home/home.html'
		});

	}]);

	// Enable HTML5-mode for $locationProvider
	app.config(['$locationProvider', function($locationProvider) {
		$locationProvider.html5Mode(true);
	}]);

})();