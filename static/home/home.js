//Initialize the angular application for this javascript page
var app = angular.module('LoLMP');

app.controller('home', function($scope, $location, $window, prediction) {
    $(document).ready(function() {

        $('#findSummoner').click(function() {
            $.ajax({
                url: "/summoner/find?name=" + $('#summonerName').val(),
                type: "get",
                success: function(response) {
                    console.log(response);

                    // set the values of the prediction service
                    prediction.summoner = response.summoner;
                    prediction.currentMatchId = response.currentMatchId;
                    prediction.blueTeam = response.blueTeam;
                    prediction.redTeam = response.redTeam;

                    // route to the prediction
                    $window.location = '/#!/prediction';
                },
                error: function(xhr) {
                //Do Something to handle error
                    console.log("invalid name");
                }
            });
        });
    });
});