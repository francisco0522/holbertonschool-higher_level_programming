#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log('code:', response && response.statusCode);
  }

  const fs = require('fs');

  fs.writeFile(file, body, function (error, data) {
    if (error) {
      return console.error(error);
    }
  });
});
