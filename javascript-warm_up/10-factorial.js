#!/usr/bin/node
// add two numbers

const argv = process.argv.slice(2);
const a = Number(argv[0]);

console.log(factor(a));

function factor (a) {
  let fact = 1;

  for (let i = 2; i <= a; i++) {
    fact *= i;
  }
  return fact;
}
