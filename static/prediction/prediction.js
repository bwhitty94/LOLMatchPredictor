//Initialize the angular application for this javascript page
var app = angular.module('LoLMP');

app.controller('prediction', function($scope, $location, prediction, $document) {
    $scope.summoner = prediction.summoner || JSON.parse(localStorage.getItem("summoner"));
    $scope.blueTeam = prediction.blueTeam || JSON.parse(localStorage.getItem("blueTeam"));
    $scope.redTeam = prediction.redTeam || JSON.parse(localStorage.getItem("redTeam"));

    localStorage.setItem("summoner", JSON.stringify($scope.summoner));
    localStorage.setItem("blueTeam", JSON.stringify($scope.blueTeam));
    localStorage.setItem("redTeam", JSON.stringify($scope.redTeam));

    if (!$scope.summoner) {
        $location.path('/');
    }

    $scope.$on('$viewContentLoaded', function(event) {
        $('.prediction').attr("style", "display: inline");
    });
});