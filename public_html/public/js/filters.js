 'use strict';
/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

iMentorApp.filter('schoolFilter', function () {
  // function to invoke by Angular each time
  // Angular passes in the `items` which is our Array
  return function (members) {
    // Create a new Array
    var filtered = [];
    // loop through existing Array
    for (var i = 0; i < members.length; i++) {
      var member = members[i];
      // check if the individual Array element begins with `a` or not
      if (member.school === "Ohtori Academy" && member.title !== "manager") {
        // push it into the Array if it does!
        filtered.push(member);
      }
    }
    // boom, return the Array after iteration's complete
    return filtered;
  };
});



iMentorApp.filter('gradeFilter9', function () {
  // function to invoke by Angular each time
  // Angular passes in the `items` which is our Array
  return function (members) {
    // Create a new Array
    var filtered = [];
    // loop through existing Array
    for (var i = 0; i < members.length; i++) {
      var member = members[i];
      // check if the individual Array element begins with `a` or not
      if (member.title === "mentee") {
	if (member.grade === 9) {
        // push it into the Array if it does!
        filtered.push(member.score);
	}
      }
    }
    // boom, return the Array after iteration's complete
    return filtered;
  };
});
iMentorApp.filter('overallScoreFilter', function () {
  // function to invoke by Angular each time
  // Angular passes in the `items` which is our Array
  return function (members) {
    // Create a new Array
    var filtered = [];
    // loop through existing Array
    for (var i = 0; i < members.length; i++) {
      var member = members[i];
      // check if the individual Array element begins with `a` or not
      if (member.title === "mentee") {
        // push it into the Array if it does!
        filtered.push(member.score);
      }
    }
    // boom, return the Array after iteration's complete
    return filtered;
  };
});
iMentorApp.filter('gradeFilter10', function () {
  // function to invoke by Angular each time
  // Angular passes in the `items` which is our Array
  return function (members) {
    // Create a new Array
    var filtered = [];
    // loop through existing Array
    for (var i = 0; i < members.length; i++) {
      var member = members[i];
      // check if the individual Array element begins with `a` or not
      if (member.title === "mentee") {
	if (member.grade === 10) {
        // push it into the Array if it does!
        filtered.push(member.score);
	}
      }
    }
    // boom, return the Array after iteration's complete
    return filtered;
  };
});

iMentorApp.filter('gradeFilter11', function () {
  // function to invoke by Angular each time
  // Angular passes in the `items` which is our Array
  return function (members) {
    // Create a new Array
    var filtered = [];
    // loop through existing Array
    for (var i = 0; i < members.length; i++) {
      var member = members[i];
      // check if the individual Array element begins with `a` or not
      if (member.title === "mentee") {
	if (member.grade === 11) {
        // push it into the Array if it does!
        filtered.push(member.score);
	}
      }
    }
    // boom, return the Array after iteration's complete
    return filtered;
  };
});

 iMentorApp.filter('gradeFilter12', function () {
  // function to invoke by Angular each time
  // Angular passes in the `items` which is our Array
  return function (members) {
    // Create a new Array
    var filtered = [];
    // loop through existing Array
    for (var i = 0; i < members.length; i++) {
      var member = members[i];
      // check if the individual Array element begins with `a` or not
      if (member.title === "mentee") {
	if (member.grade === 12) {
        // push it into the Array if it does!
        filtered.push(member.score);
	}
      }
    }
    // boom, return the Array after iteration's complete
    return filtered;
  };
});

  iMentorApp.filter('staffFilter', function () {
  // function to invoke by Angular each time
  // Angular passes in the `items` which is our Array
  return function (members) {
    // Create a new Array
    var filtered = [];
    // loop through existing Array
    for (var i = 0; i < members.length; i++) {
      var member = members[i];
      // check if the individual Array element begins with `a` or not
      if (member.title === "mentor" && member.underStaffMember === "Anne Hathaway") {
        // push it into the Array if it does!
        filtered.push(member);
      }
    }
    // boom, return the Array after iteration's complete
    return filtered;
  };
});

  iMentorApp.filter('badScoreFilter', function () {
  // function to invoke by Angular each time
  // Angular passes in the `items` which is our Array
  return function (members) {
    // Create a new Array
    var filtered = [];
    // loop through existing Array
    for (var i = 0; i < members.length; i++) {
      var member = members[i];
      // check if the individual Array element begins with `a` or not
      if (member.averageScore < 3 && member.title !== "manager") {
        // push it into the Array if it does!
        filtered.push(member);
      }
    }
    // boom, return the Array after iteration's complete
    return filtered;
  };
});

  iMentorApp.filter('goodScoreFilter', function () {
  // function to invoke by Angular each time
  // Angular passes in the `items` which is our Array
  return function (members) {
    // Create a new Array
    var filtered = [];
    // loop through existing Array
    for (var i = 0; i < members.length; i++) {
      var member = members[i];
      // check if the individual Array element begins with `a` or not
      if (member.score < 3) {
        // push it into the Array if it does!
        filtered.push(member);
      }
    }
    // boom, return the Array after iteration's complete
    return filtered;
  };
});

