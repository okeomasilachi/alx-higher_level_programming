#!/usr/bin/node

const rq = require('request');
const fs = require('fs');

if (process.argv.length < 4) {
  process.exit();
}

// Request URL
const url = process.argv[2];
const path = process.argv[3];

rq(url, (error, response) => {
  if (error) {
    console.error(error);
  }

  const value = response.body;
  fs.writeFile(path, value, 'utf-8', (error, data) => {
    if (error) {
      console.error(error);
    }
  });
});
