/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

var iMentorApp = angular.module('iMentorApp', []);
 //note that you need to use $scope and $http in this controller so they must be listed
 //as dependencies
iMentorApp.controller('mentorCtrl', ['$scope', '$http', function ($scope, $http) {
    
 $http.get('js/data/members.json').success(function(data) {
    $scope.members = data;
    
  });
  $scope.orderProp = 'id';
  
  $http.get('js/data/emails.json').success(function(data2){
      $scope.emails = data2;
  });

}]).controller('adminCtrl', ['$scope', '$http', function ($scope, $http) {     
      
       $http.get('js/data/members.json').success(function(data) {
            $scope.members = data;
        });
        
       
        
}]).controller('staffCtrl', ['$scope', '$http', function ($scope, $http) {
    
       $http.get('js/data/members.json').success(function(data) {
            $scope.members = data;
        });

 }]);
 