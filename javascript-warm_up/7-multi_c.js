#!/usr/bin/node
// i love c

const argv = process.argv.slice(2);
let count = 0;
let i = 1;

if (Number.isInteger(Number(Math.trunc(argv[0])))) {
  count = Math.trunc(argv[0]);
} else {
  console.log('Missing number of occurrences');
}

while (i <= count) {
  console.log('C is fun');
  i++;
}
