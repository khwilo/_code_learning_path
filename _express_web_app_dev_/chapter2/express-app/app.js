var http = require('http');

var express = require('express');

// create an instance of Express
var app = express();

// start the app
http.createServer(app).listen(3000, function () {
    console.log('Express app started');
});

// A route for the home page
app.get('/', function (req, res){
    res.send('<h1>Welcome!</h1>');
});