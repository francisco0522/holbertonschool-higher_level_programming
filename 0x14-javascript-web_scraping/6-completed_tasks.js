#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonBody = JSON.parse(body);
    let task = 0;
    let y = 1;
    const result = {};
    for (let i = 0; i < jsonBody.length; i++) {
      if (i > 0) {
        y = jsonBody[i - 1].userId;
      }
      if (jsonBody[i].userId !== y) {
        result[y] = task;
        task = 0;
      }
      if (jsonBody[i].completed === true) {
        task = task + 1;
      }
    }
    result[y] = task;
    console.log(result);
  }
});
