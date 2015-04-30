(function() {

	var app = angular.module('mp', [
		'ngRoute',
		'ngResource',

		'mp.createPoll'
	]);

	// Configure the $routeProvider's routes
	app.config(function($routeProvider) {

		// Route handlers
		$routeProvider.when('/', {
			templateUrl: '/home/home.html'
		}).when('/poll/:pollId', {
			templateUrl: '/poll-detail/poll-detail.html',
			resolve: {
				poll: function(Poll, $route) {
					var pollId = $route.current.params.pollId;
					return Poll.get({ pollId: pollId }).$promise;
				}
			},
			controller: function($scope, $routeParams, poll) {
				$scope.init = function() {
					$scope.poll = poll;

					$scope.showPreview = ($routeParams.preview == 'true') || false;
				};


				// Init
				$scope.init();
			}
		});

	});

	// Enable HTML5-mode for $locationProvider
	app.config(['$locationProvider', function($locationProvider) {
		$locationProvider.html5Mode(true);
	}]);

	app.controller('appCtrl', function($scope, $location) {
		$scope.init = function() {
			$scope.searchPollIdentifier = '';
		};

		$scope.findPollIdentifier = function() {
			$location.path('/poll/'+$scope.searchPollIdentifier);
		};


		// Init
		$scope.init();
	});

})();