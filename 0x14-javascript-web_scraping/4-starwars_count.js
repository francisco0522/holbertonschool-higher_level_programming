#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); } else {
    let x = 0;
    for (const film of body.results) {
      for (const character of film.characters) {
        if (character === 'https://swapi-api.hbtn.io/api/people/18/') {
          x += 1;
        }
      }
    }
    console.log(x);
  }
});
