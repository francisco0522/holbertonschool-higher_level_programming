#!/usr/bin/node
const url = process.argv[2];

const fs = require('fs');

fs.readFile(url, 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
