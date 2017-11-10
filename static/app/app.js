'use strict';

var app = angular.module('LoLMP', ['ngRoute']);

//This is how Angular determines what page to display based on the URL.
//Note: The controller will be in the same parent folder as the templateUrl but in the js folder
//"css" value is optional
app.config(['$routeProvider', function($routeProvider) {
    $routeProvider
    //This is the home page
    .when('/', {
       templateUrl: 'static/home/home.html',
       controller: 'home',
    })
    //Page to show the prediction results
    .when('/prediction', {
        templateUrl: 'static/prediction/prediction.html',
        controller: 'prediction',
    })
    //If none of the "when"s are matched then it defaults to the home page.
    .otherwise({
       redirectTo: '/'
    });
}]);