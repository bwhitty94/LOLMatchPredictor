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
        console.log(prediction.blueTeam.concat(prediction.redTeam));
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
            console.log('success');
            prediction.value = response.value;
        }, function errorCallback(response) {
            console.log(response);
        });

//        $.ajax({
//            url: "/predict/get",
//            method: "POST",
//            contentType: "application/json; charset=utf-8",
//            data: {
//                'team': prediction.blueTeam.concat(prediction.redTeam)
//            },
//            success: function(response) {
//                prediction.value = response.value;
//                console.log("val: " + prediction.value);
//            },
//            error: function(xhr) {
//            //Do Something to handle error
//                console.log(xhr);
//            }
//        });
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

                        getPrediction();

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