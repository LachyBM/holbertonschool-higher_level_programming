#!/usr/bin/node
// value of the argument

const argv = process.argv.slice(2);

if (!([0] in argv)) {
  console.log('No argument');
} else {
  console.log(argv[0]);
}
