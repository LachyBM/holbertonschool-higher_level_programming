#!/usr/bin/node
// add from the outside world

function add (a, b) {
  const result = a + b;
  return result;
}

module.exports = { add };
