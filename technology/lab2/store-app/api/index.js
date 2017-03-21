/**
 * Created by Drapegnik on 21.03.17.
 */

var express = require('express');
var router = express.Router();

router.get('/', function (req, res, next) {
  res.send('Hello from api!');
});

module.exports = router;
