#!/usr/bin/node
/**
 * Square that defines a square and inherits from Square of 5-square.js
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
