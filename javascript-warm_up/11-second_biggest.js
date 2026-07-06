#!/usr/bin/node
// add two numbers

const argv = process.argv.slice(2);
const argc = process.argv.length;
let biggest = 0;
let second = 0;
if (argc > 3) {
  for (let i = 0; i <= argc; i++) {
    if (Number(argv[i]) >= biggest) {
      second = biggest;
      biggest = argv[i];
    } else if (Number(argv[i]) >= second) {
      second = argv[i];
    }
  }
}
console.log(second);
