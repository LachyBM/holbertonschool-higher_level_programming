#!/usr/bin/node
// add two numbers

const argv = process.argv.slice(2);
const a = Number(argv[0]);
let fact = 1;

for (let i = 2; i <= a; i++) {
  fact *= i;
}

console.log(fact);
