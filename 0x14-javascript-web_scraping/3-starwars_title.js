#!/usr/bin/node

const rq = require('request');

if (process.argv.length < 3) {
  process.exit();
}

if (isNaN(process.argv[2])) {
  process.exit();
}

// Request URL
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

rq(url, (error, response) => {
  if (error) {
    console.error(error);
  }

  let value = response.toJSON();
  value = JSON.parse(value.body);
  console.log(value.title);
});
