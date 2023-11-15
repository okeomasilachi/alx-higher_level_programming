#!/usr/bin/node

const l = require('./100-data.js').list;

console.log(l);
console.log(l.map((v, i) => v * i));
