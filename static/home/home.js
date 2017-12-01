//Initialize the angular application for this javascript page
var app = angular.module('LoLMP');

app.controller('home', function($rootScope, $scope, $location, $window, $compile, prediction, $http) {
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
        $http({
            method: 'POST',
            url: '/predict/get',
            headers: {
                'Content-Type': 'application/json'
            },
            data: {
                'team': prediction.blueTeam.concat(prediction.redTeam)
            }
        }).then(function successCallback(response) {
            prediction.value = response.data.value;

            // route to the prediction
            $window.location = '/#!/prediction';
        }, function errorCallback(response) {
            console.log(response);
        });
    };

    $(document).ready(function() {
        $("#summonerName, #pastGame").keyup(function(event) {
            if (event.keyCode === 13) {
                $("#findSummoner").click();
            }
        });

        $("#viewPastGame").click(function() {
            $http({
                method: 'POST',
                url: '/predict/past',
                headers: {
                    'Content-Type': 'application/json'
                },
                data: {
                    'gameNum': $scope.pastGame
                }
            }).then(function successCallback(response) {
                // set the values of the prediction service
                prediction.blueTeam = response.data.blueTeam;
                prediction.redTeam = response.data.redTeam;
                prediction.value = response.data.value;

                // route to the prediction
                $window.location = '/#!/prediction';
            }, function errorCallback(response) {
                console.log(response);
            });
        });

        $("#findSummoner").click(function() {
            $.ajax({
                url: "/summoner/find?name=" + $('#summonerName').val(),
                type: "get",
                success: function(response) {
                    if (response.error) {
                        createAlert(response.error);
                    }
                    else {
                        // set the values of the prediction service
                        prediction.blueTeam = response.blueTeam;
                        prediction.redTeam = response.redTeam;

                        getPrediction();
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