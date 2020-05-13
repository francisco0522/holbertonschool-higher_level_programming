#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let task = 0;
    let y = 1;
    const res = {};
    for (let i = 0; i < body.length; i++) {
      if (i > 0) {
        y = body[i - 1].userId;
      }
      if (body[i].userId !== y) {
        res[y] = task;
        task = 0;
      }
      if (body[i].completed === true) {
        task = task + 1;
      }
    }
    res[y] = task;
    console.log(res);
  }
});
