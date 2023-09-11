#!/usr/bin/node

const arg = process.argv[2]; // Get the first argument

if (arg !== undefined) {
  console.log(arg);
} else {
  console.log('No argument');
}
