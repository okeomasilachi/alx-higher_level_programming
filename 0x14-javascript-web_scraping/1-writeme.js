#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 4) {
  process.exit();
}

const path = process.argv[2];
const string = process.argv[3];

fs.writeFile(path, string, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  }
});
