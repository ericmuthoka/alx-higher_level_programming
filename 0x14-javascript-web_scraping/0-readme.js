#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from the command line arguments

if (!filePath) {
  console.error('Usage: node read-file.js <file-path>');
  process.exit(1);
}

// Read the file in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // An error occurred during reading the file
    console.error(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});

