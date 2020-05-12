#!/usr/bin/node
const url = process.argv[2];
const textString = process.argv[3];

const fs = require('fs');

fs.writeFile(url, textString, function (error, data) {
  if (error) {
    console.log(error);
  }
});
