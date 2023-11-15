#!/usr/bin/node

class Rectangle {
  width;
  height;

  constructor (w, h) {
    this.height = h;
    this.width = w;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
