#!/usr/bin/node
const a = parseInt(process.argv[2], 10);
let b = 1;

function factorial (a) {
  for (let i = 0; i < a; i++) {
    const fact = a - i;
    b = b * fact;
  }
  console.log(b);
}
factorial(a);
