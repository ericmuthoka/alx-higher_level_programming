#!/usr/bin/node

function addMeMaybe(number, theFunction) {
  number++;
  theFunction(number);
}

module.exports.addMeMaybe = addMeMaybe; // Export the function

// Example usage:
// const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
// addMeMaybe(4, function (nb) {
//   console.log('New value: ' + nb);
// });
