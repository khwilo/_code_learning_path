var http = require('http');

var express = require('express');

// create an instance of Express
var app = express();

// set the view engine
app.set('view engine', 'jade');
// locate the view files
app.set('views', './views');

// A route for the home page
app.get('/', function (req, res){
    res.render('index');
});

// A route for /say-hello
app.get('/say-hello', function (req,res) {
    res.render('hello');
});

app.get('/test', function (req, res) {
    res.send('this is a test');
});

// start the app
http.createServer(app).listen(3000, function () {
    console.log('Express app started');
});