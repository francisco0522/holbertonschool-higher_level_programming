#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, { json: true }, (err, res, body) => {
  if (err) { console.log('code:', res.statusCode); } else {
    for (const film of body.characters) {
      request(film, { json: true }, (err, res, body) => {
        if (err) { console.log('code:', res.statusCode); } else {
          console.log(body.name);
        }
      });
    }
  }
});
