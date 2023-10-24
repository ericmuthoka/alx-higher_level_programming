#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Get the movie ID from the first command line argument

if (!movieId) {
  console.error('Usage: ./3-starwars_title.js <movie-ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      console.log(movie.title);
    } else {
      console.error(`Request failed with status code: ${response.statusCode}`);
    }
  }
});
