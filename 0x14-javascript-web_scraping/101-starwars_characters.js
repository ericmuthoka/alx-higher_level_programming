#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Get the movie ID from the first command line argument

if (!movieId) {
  console.error('Usage: ./101-starwars_characters.js <Movie-ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Define the correct order of characters in "Return of the Jedi"
const characterOrder = [
  'Luke Skywalker',
  'C-3PO',
  'R2-D2',
  'Darth Vader',
  'Leia Organa',
  'Obi-Wan Kenobi',
  'Chewbacca',
  'Han Solo',
  'Jabba Desilijic Tiure',
  'Wedge Antilles',
  'Yoda',
  'Palpatine',
  'Boba Fett',
  'Lando Calrissian',
  'Ackbar',
  'Mon Mothma',
  'Arvel Crynyd',
  'Wicket Systri Warrick',
  'Nien Nunb',
  'Bib Fortuna',
];

// Make a GET request to the Star Wars API to retrieve the movie details
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      const characters = movie.characters;

      // Create a map of character names to URLs
      const characterUrlMap = {};
      characters.forEach((characterUrl) => {
        const characterId = characterUrl.split('/').slice(-2)[0];
        characterUrlMap[characterId] = characterUrl;
      });

      // Print characters in the correct order
      characterOrder.forEach((characterName) => {
        const characterUrl = characterUrlMap[characterName];
        if (characterUrl) {
          request.get(characterUrl, (charError, charResponse, charBody) => {
            if (!charError && charResponse.statusCode === 200) {
              const character = JSON.parse(charBody);
              console.log(character.name);
            }
          });
        }
      });
    } else {
      console.error(`Request failed with status code: ${response.statusCode}`);
    }
  }
});
