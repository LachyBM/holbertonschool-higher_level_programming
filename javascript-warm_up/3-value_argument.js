#!/usr/bin/node
// value of the argument

const argc = process.argv.length;
const argv = process.argv.slice(2);

if (argc === 2) {
  console.log('No argument');
} else {
  console.log(argv.join(' '));
}
