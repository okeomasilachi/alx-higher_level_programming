#!/usr/bin/node

const [fArg] = process.argv.slice(2);

const num = parseInt(fArg, 10);

if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
