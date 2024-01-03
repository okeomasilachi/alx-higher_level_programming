#!/usr/bin/node

const rq = require('request');

if (process.argv.length < 3) {
  process.exit();
}

// Request URL
const url = process.argv[2];

rq(url, (error, response) => {
  if (error) {
    console.error(error);
  }
  // Printing status code
  console.log('code:', response.statusCode);
});
