#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }

  const fs = require('fs');

  fs.writeFile(file, body, function (error, data) {
    if (error) {
      console.log(error);
    }
  });
});
