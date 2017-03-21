/**
 * Created by Drapegnik on 21.03.17.
 */

var express = require('express');
var path = require('path');
var fs = require('fs');
var logger = require('morgan');
var bodyParser = require('body-parser');
var http = require('http');
var cors = require('cors');

var client = JSON.parse(fs.readFileSync('.angular-cli.json', 'utf8'));
var publicPath = path.join(__dirname, client.apps[0].outDir);
var app = express();
var api = require('./api');

app.use(cors());
app.use(logger('dev'));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
app.use(express.static(publicPath));

app.use('/api', api);

app.use(function (req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

app.use(function (err, req, res, next) {
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  console.error(err.message);
  res.status(err.status || 500);
  res.send(err.message);
});

app.get('*', function (req, res) {
  res.sendFile(path.join(publicPath, 'index.html'));
});

var server = http.createServer(app);
server.listen(3000, function () {
  console.log('Server running at http://localhost:3000');
});
