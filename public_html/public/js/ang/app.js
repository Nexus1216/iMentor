'use strict';

/* App Module */

var iMentorApp = angular.module('iMentor', [
  'mentorCtrl', 'adminCtrl', 'staffCtrl', 'iMentorFilters'
]);

iMentorApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/index', {
        templateUrl: 'index.html',
        controller: 'mentorCtrl'
      });
  }]);