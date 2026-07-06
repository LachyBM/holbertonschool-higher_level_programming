#!/usr/bin/node
// arguments

const argc = process.argv.length;

if (argc === 2) {
  console.log('No arguments');
} else if (argc === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
