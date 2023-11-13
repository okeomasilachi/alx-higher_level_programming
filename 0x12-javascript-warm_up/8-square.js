#!/usr/bin/node

const [args] = process.argv.slice(2);

const num = parseInt(args);

if (!isNaN(num)) {
  for (let i = 0; i < num; i++) { console.log('X'.repeat(num)); }
} else {
  console.log('Missing size');
}
