#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (err, res, body) => {
  if (err) { console.log('code:', res.statusCode); } else {
    let x = 0;
    for (const film of body.results) {
      for (const character of film.characters) {
        if (character.endsWith('/18/')) {
          x += 1;
        }
      }
    }
    console.log(x);
  }
});
