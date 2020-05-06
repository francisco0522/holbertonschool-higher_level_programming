#!/usr/bin/node
let big = 0;
let second = 0;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (big < process.argv[i]) {
      second = big;
      big = process.argv[i];
    }
    if (big === process.argv[i]) {
      second = big;
    }
  }
  console.log(second);
}
