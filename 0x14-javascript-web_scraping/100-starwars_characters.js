#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Get the movie ID from the first command line argument

if (!movieId) {
  console.error('Usage: ./100-starwars_characters.js <Movie-ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API to retrieve the movie details
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      const characterUrls = movie.characters;

      // Fetch and print the names of characters
      characterUrls.forEach((characterUrl) => {
        request.get(characterUrl, (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const character = JSON.parse(charBody);
            console.log(character.name);
          }
        });
      });
    } else {
      console.error(`Request failed with status code: ${response.statusCode}`);
    }
  }
});
