(function() {

	var app = angular.module('mp.createPoll', []);

	app.directive('createPoll', function(Poll) {
		return {
			restrict: 'AE',
			templateUrl: '/create-poll/detail.html',
			controller: function($scope, $location) {
				$scope.init = function() {
					$scope.newPoll = {
						responses: [
							{
								name: ''
							}, {
								name: ''
							}
						],
						question: ''
					}
				};

				$scope.addResponse = function() {
					$scope.newPoll.responses.push({
						name: ''
					});
				};

				$scope.removeResponse = function(index) {
					$scope.newPoll.responses.splice(index, 1);
				};

				$scope.createPoll = function() {
					console.log('[mp.createPoll] $scope.createPoll: Called.');

					var responses = [];

					for (var i = 0; i < $scope.newPoll.responses.length; i++) {
						responses.push($scope.newPoll.responses[i].name);
					}

					Poll.create(null, {
						question: $scope.newPoll.question,
						responses: responses
					}, function(response) {
						// HTTP 200-299 Status
						if (angular.isObject(response)) {
							if (response.hasOwnProperty('id')) {
								$location.path('/poll/'+response.id).search({
									preview: true
								});
							}
						}
						console.log(response);
					}, function(response) {
						// Error
						console.log(response);
					});
				};


				// Init
				$scope.init();
			}
		};
	});

	app.directive('pollDetail', function(Poll) {
		return {
			restrict: 'AE',
			templateUrl: '/poll-detail/detail.html'
		};
	});

	app.directive('pollPreview', function(Poll) {
		return {
			restrict: 'AE',
			templateUrl: '/poll-detail/preview.html'
		};
	});

	app.factory('Poll', function($resource) {
		return $resource('/api/poll/:pollId', null, {
			create: {
				method: 'POST'
			}
		});
	})

})();