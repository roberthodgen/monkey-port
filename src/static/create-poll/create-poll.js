(function() {

	var app = angular.module('mp.createPoll', []);

	app.directive('createPoll', function() {
		return {
			restrict: 'AE',
			templateUrl: '/create-poll/detail.html'
		};
	});

})();