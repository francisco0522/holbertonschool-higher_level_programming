#!/usr/bin/node
let x = '';

class Square extends require('./5-square') {
  constructor (s) {
    super(s, s);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          x += 'X';
        } else {
          x += c;
        }
      }
      console.log(x);
      x = '';
    }
  }
}

module.exports = Square;
