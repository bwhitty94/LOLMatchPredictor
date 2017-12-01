//Initialize the angular application for this javascript page
var app = angular.module('LoLMP');

app.controller('home', function($rootScope, $scope, $location, $window, $compile, prediction) {
    // creates an alert and shows the message
    function createAlert(message) {
        var alert = $('#alert');
        var html;

        $scope.error = message;

        // load alert.html and apply the scope to show errors
        $.get("/static/home/alert.html", function(data) {
            html = data;
        })
        .done(function() {
            alert.html($compile(html)($scope));
            $scope.$apply();
        });
    };

    function getPrediction() {
        $.ajax({
            url: "/prediction",
            type: "get",
            success: function(response) {
                prediction.value = response.value;
            },
            error: function(xhr) {
            //Do Something to handle error
                console.log("error");
            }
        });
    };

    $(document).ready(function() {
        $("#summonerName").keyup(function(event) {
            if (event.keyCode === 13) {
                $("#findSummoner").click();
            }
        });

        $('#findSummoner').click(function() {
            $.ajax({
                url: "/summoner/find?name=" + $('#summonerName').val(),
                type: "get",
                success: function(response) {
                    if (response.error) {
                        createAlert(response.error);
                    }
                    else {
                        // set the values of the prediction service
                        prediction.summoner = response.summoner;
                        prediction.currentMatchId = response.currentMatchId;
                        prediction.blueTeam = response.blueTeam;
                        prediction.redTeam = response.redTeam;

                        // route to the prediction
                        $window.location = '/#!/prediction';
                    }
                },
                error: function(xhr) {
                //Do Something to handle error
                    console.log("error");
                }
            });
        });
    });
});