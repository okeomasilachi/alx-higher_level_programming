#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node movie_characters.js <Movie_ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Unexpected response: ${response.statusCode}`);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  if (characterUrls.length === 0) {
    console.log(`No characters found for Movie ID ${movieId}`);
    process.exit(0);
  }

  // Use async/await to ensure characters are printed in order
  (async () => {
    for (const characterUrl of characterUrls) {
      const characterData = await fetchCharacterData(characterUrl);
      console.log(characterData.name);
    }
  })();
});

function fetchCharacterData (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        // Use an Error object for better error handling
        reject(new Error(charError));
      } else if (charResponse.statusCode !== 200) {
        // Use an Error object for better error handling
        reject(new Error(`Unexpected response for character: ${charResponse.statusCode}`));
      } else {
        const characterData = JSON.parse(charBody);
        resolve(characterData);
      }
    });
  });
}
