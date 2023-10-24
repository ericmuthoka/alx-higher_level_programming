#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from the first command line argument
const characterId = 18; // ID for Wedge Antilles

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API-URL>');
  process.exit(1);
}

// Make a GET request to the Star Wars API to retrieve the films
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const films = JSON.parse(body).results;
      const count = films.filter((film) => film.characters.includes(characterId)).length;
      console.log(count);
    } else {
      console.error(`Request failed with status code: ${response.statusCode}`);
    }
  }
});
