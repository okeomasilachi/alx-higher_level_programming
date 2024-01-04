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
  const dict = {};
  let value = response.toJSON();
  value = JSON.parse(value.body);
  value.forEach(element => {
    if (Object.hasOwnProperty.call(dict, element.userId)) {
      if (element.completed === true) {
        dict[element.userId] = dict[element.userId] + 1;
      }
    } else {
      dict[element.userId] = 0;
    }
  });
  console.log(dict);
});
