(function() {

	var app = angular.module('mp.createPoll', []);

	app.directive('createPoll', function() {
		return {
			restrict: 'AE',
			templateUrl: '/create-poll/detail.html',
			controller: function($scope) {
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
				};


				// Init
				$scope.init();
			}
		};
	});

})();