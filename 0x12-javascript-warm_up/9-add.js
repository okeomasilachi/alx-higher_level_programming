#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const args = process.argv.slice(2);

const num1 = parseInt(args[0]);
const num2 = parseInt(args[1]);

console.log(add(num1, num2));
