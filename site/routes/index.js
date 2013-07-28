
/*
 * GET home page.
 */

var fileViewer = require("../lib/fileViewer.js");
var files = fileViewer.listFiles();
exports.index = function(req, res){
  res.render('index', { title: 'files', files: files });
};
