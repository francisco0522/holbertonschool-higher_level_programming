#!/usr/bin/node
let x = '';

class Square extends require('./5-square') {
  constructor (s) {
    super(s, s);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
