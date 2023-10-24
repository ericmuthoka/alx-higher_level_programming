#!/usr/bin/node

const request = require('request');

const url = process.argv[2]; // Get the URL from the first command line argument

if (!url) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Print the status code from the response
    console.log(`code: ${response.statusCode}`);
  }
});

