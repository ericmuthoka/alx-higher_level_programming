#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Get the movie ID from the first command line argument

if (!movieId) {
  console.error('Usage: ./101-starwars_characters.js <Movie-ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Map character IDs to their correct order in the movie
const characterOrder = {
  1: 3,   // Luke Skywalker
  2: 13,  // C-3PO
  3: 2,   // R2-D2
  4: 4,   // Darth Vader
  5: 5,   // Leia Organa
  6: 10,  // Obi-Wan Kenobi
  7: 6,   // Chewbacca
  8: 7,   // Han Solo
  9: 11,  // Jabba Desilijic Tiure
  10: 12, // Wedge Antilles
  11: 14, // Yoda
  12: 15, // Palpatine
  13: 16, // Boba Fett
  14: 8,  // Ackbar
  15: 17, // Mon Mothma
  16: 18, // Arvel Crynyd
  17: 19, // Wicket Systri Warrick
  18: 20, // Nien Nunb
  19: 21, // Bib Fortuna
};

// Make a GET request to the Star Wars API to retrieve the movie details
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      const characterUrls = movie.characters;

      // Fetch and print the names of characters in movie order
      characterUrls.sort((a, b) => characterOrder[a.split('/').pop()] - characterOrder[b.split('/').pop()]);
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
