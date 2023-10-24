#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2]; // Get the URL from the first command line argument
const filePath = process.argv[3]; // Get the file path from the second command line argument

if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js <URL> <file-path>');
  process.exit(1);
}

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      // Write the response to the file in utf-8 encoding
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          console.error(err);
        }
      });
    } else {
      console.error(`Request failed with status code: ${response.statusCode}`);
    }
  }
});
