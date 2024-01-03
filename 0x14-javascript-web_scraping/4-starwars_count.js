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

  let num = 0;
  let value = response.toJSON();
  value = JSON.parse(value.body);
  value = value.results;
  for (let i = 0; i < value.length; i++) {
    const char = value[i].characters;
    for (let j = 0; j < char.length; j++) {
      if (char[j] === 'https://swapi-api.alx-tools.com/api/people/18/') {
        num++;
      }
    }
  }
  console.log(num);
});
