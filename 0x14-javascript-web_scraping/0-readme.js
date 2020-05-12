#!/usr/bin/node
const url = process.argv[2];
/* File System Object */
var fs = require('fs');

/* Read File */
fs.readFile(url, 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
