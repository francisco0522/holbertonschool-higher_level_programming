#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (err, res, body) => {
  if (err) { console.log(err); } else {
    const result = {};
    for (const todo of body) {
      if (todo.completed) {
        if (result[todo.userId]) {
          result[todo.userId] += 1;
        } else {
          result[todo.userId] = 1;
        }
      }
    }
    console.log(result);
  }
});
