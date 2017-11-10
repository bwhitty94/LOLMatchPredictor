//Initialize the angular application for this javascript page
var app = angular.module('LoLMP');

app.controller('home', function($scope, $location) {
    $(document).ready(function() {

        $('#findSummoner').click(function() {
            $.ajax({
                url: "/summoner/find?name=" + $('#summonerName').val(),
                type: "get",
                success: function(response) {
                    console.log("name is: " + response);
                    $location.path('/prediction')
                },
                error: function(xhr) {
                //Do Something to handle error
                }
            });
        });
    });
});