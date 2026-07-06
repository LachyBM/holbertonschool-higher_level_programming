#!/usr/bin/node
// value of the argument

const argv = process.argv.slice(2);

if (Number.isInteger(Number(Math.trunc(argv[0])))) {
  console.log('My number: ' + Math.trunc(argv[0]));
} else {
  console.log('Not a number');
}
