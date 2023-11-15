#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(w)) {
      this.height = h;
      this.width = w;
    }
  }
}

module.exports = Rectangle;
