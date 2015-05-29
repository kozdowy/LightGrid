var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
  res.render('index', { title: 'WE <3 KENNY' });
});

router.post('/submit', function(req, res){
  var data = req.body.content;
  console.log(typeof data);
  process.stdout.write(data + "\n");
  res.location('/');
  res.redirect('/');
});

module.exports = router;
