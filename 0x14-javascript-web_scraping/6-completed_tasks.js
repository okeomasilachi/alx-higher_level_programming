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
    const { userId, completed } = element;
    if (Object.hasOwnProperty.call(dict, userId)) {
      if (completed === true) {
        dict[userId]++;
      }
    } else if (!Object.hasOwnProperty.call(dict, userId) && completed) {
      dict[userId] = 1;
    }
  });
  console.log(dict);
});
