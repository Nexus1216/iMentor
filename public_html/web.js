/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */



var express = require('express');
var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var app = express();
var fs = require('fs');
var sys = require('sys');
app.use(express.bodyParser({keepExtensions: true, uploadDir: '/myFiles', limit: '50mb'}));
app.use(express.static(__dirname + '/public'));
app.use(express.cookieParser('nofoaijoisjodsaiunsadouniucnsacun'));
app.use(express.session({cookie: {httpOnly: false}, key: 'youtrkey'}));

var server = app.listen(8523, function() {
    console.log('Listening on port %d', server.address().port);
});

var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function callback () {
  console.log('Opened up the connection okay.');
});

mongoose.connect('mongodb://mikachama:Haruka10@ds033419.mongolab.com:33419/inventory');