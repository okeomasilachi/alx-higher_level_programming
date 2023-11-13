#!/usr/bin/node

const [args] = process.argv.slice(2);

if (args !== undefined) {
  console.log(args);
} else {
  console.log('No argument');
}
