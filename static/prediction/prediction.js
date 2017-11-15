//Initialize the angular application for this javascript page
var app = angular.module('LoLMP');

app.controller('prediction', function($scope, $location, prediction) {
    $scope.summoner = prediction.summoner;
    $scope.blueTeam = prediction.blueTeam;
    $scope.redTeam = prediction.redTeam;

    console.log("size: " + $scope.blueTeam.length);
});