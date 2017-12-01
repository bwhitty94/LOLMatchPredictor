//Initialize the angular application for this javascript page
var app = angular.module('LoLMP');

function setPredictionColor(team) {
    var prediction = $('#prediction');
    prediction.removeClass("blueTeam");
    prediction.removeClass("redTeam");
    prediction.removeClass("neutral");

    switch(team) {
        case "blue":
            prediction.addClass("blueTeam");
            break;

        case "red":
            prediction.addClass("redTeam");
            break;

        case "neutral":
            prediction.addClass("neutral");
            break;

        default:
            break;
    };
};

app.controller('prediction', function($scope, $location, prediction, $document) {
    $scope.summoner = prediction.summoner || JSON.parse(localStorage.getItem("summoner"));
    $scope.blueTeam = prediction.blueTeam || JSON.parse(localStorage.getItem("blueTeam"));
    $scope.redTeam = prediction.redTeam || JSON.parse(localStorage.getItem("redTeam"));

    // generate prediction
    var prediction;
    var team;

    prediction = prediction.value || JSON.parse(localStorage.getItem("prediction"));

    switch(prediction) {
        case 1:
            $scope.predictionString = "Red Team is strongly favored to win!";
            team = "red";
            break;

        case 2:
            $scope.predictionString = "Red Team is marginally favored to win!";
            team = "red";
            break;

        case 3:
            $scope.predictionString = "Neither team is favored to win!";
            team = "neutral";
            break;

        case 4:
            $scope.predictionString = "Blue Team is marginally favored to win!";
            team = "blue";
            break;

        case 5:
            $scope.predictionString = "Blue Team is strongly favored to win!";
            team = "blue";
            break;

        default:
            $scope.predictionString = "Unable to make a conclusion!";
    };

    setPredictionColor(team);

    // set local storage so prediction screen persists through refresh
    localStorage.setItem("summoner", JSON.stringify($scope.summoner));
    localStorage.setItem("blueTeam", JSON.stringify($scope.blueTeam));
    localStorage.setItem("redTeam", JSON.stringify($scope.redTeam));
    localStorage.setItem("prediction", JSON.stringify(prediction));

    if (!$scope.summoner) {
        $location.path('/');
    }

    $scope.$on('$viewContentLoaded', function(event) {
        $('.prediction').attr("style", "display: inline");
    });
});