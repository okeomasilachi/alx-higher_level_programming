#!/usr/bin/node

const myVar = 'C is fun';

const [args] = process.argv.slice(2);

const num = parseInt(args);

if (!isNaN(num)) {
  for (let i = 0; i < num; i++) { console.log(myVar); }
} else {
  console.log('Missing number of occurrences');
}
