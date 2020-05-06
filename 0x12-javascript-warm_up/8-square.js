#!/usr/bin/node
let x = '';
if (isNaN(parseInt(process.argv[2], 10)) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2], 10); i++) {
    for (let y = 0; y < parseInt(process.argv[2], 10); y++) {
      x += 'X';
    }
    console.log(x);
    x = '';
  }
}
