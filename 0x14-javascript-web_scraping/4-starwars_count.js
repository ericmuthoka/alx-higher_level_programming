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
      let count = 0;

      // Iterate through the films and check if Wedge Antilles is present in any of them
      films.forEach((film) => {
        const characters = film.characters;
        if (characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
          count++;
        }
      });

      console.log(count);
    } else {
      console.error(`Request failed with status code: ${response.statusCode}`);
    }
  }
});
