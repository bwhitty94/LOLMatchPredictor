//Initialize the angular application for this javascript page
var app = angular.module('LoLMP');

app.controller('prediction', function($scope, $location, prediction, $document) {
    $scope.summoner = prediction.summoner;
    $scope.blueTeam = prediction.blueTeam;
    $scope.redTeam = prediction.redTeam;

    $scope.$on('$viewContentLoaded', function(event) {
        $('.prediction').attr("style", "display: inline");
    });
});