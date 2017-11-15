//Initialize the angular application for this javascript page
var app = angular.module('LoLMP');

app.controller('home', function($scope, $location, $window, prediction) {
    $(document).ready(function() {

        $('#findSummoner').click(function() {
            $.ajax({
                url: "/summoner/find?name=" + $('#summonerName').val(),
                type: "get",
                success: function(response) {
                    console.log("name is: " + response);
                    console.log("blueTeam: " + response.champ);
                    prediction.summoner = response.summoner;
                    prediction.current_match_id = response.current_match_id;
                    $window.location = '/#!/prediction';
                },
                error: function(xhr) {
                //Do Something to handle error
                    console.log("invalid name");
                }
            });
            console.log("hello?");
            $location.path('/');
        });
    });
});