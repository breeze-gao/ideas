var fs = require("fs");

exports.listFiles = listFiles;

function listFiles(path) {
  path = path || "/";
  return fs.readdirSync(path);
}
