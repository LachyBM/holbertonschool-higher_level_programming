#!/usr/bin/node
// add two numbers

const argv = process.argv.slice(2);
const a = Number(argv[0]);
const b = Number(argv[1]);

console.log(add(a, b));

function add (a, b) {
  return a + b;
}
