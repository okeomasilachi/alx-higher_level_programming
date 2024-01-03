#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 3) {
  process.exit();
}

const path = process.argv[2];

fs.readFile(path, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
