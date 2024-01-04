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

  if (response.sC !== 200) {
    console.error(`Unexpected response: ${response.sC}`);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const cUrls = movieData.characters;

  if (cUrls.length === 0) {
    console.log(`No characters found for Movie ID ${movieId}`);
    process.exit(0);
  }

  (async () => {
    for (const cUrl of cUrls) {
      const cI = await fCI(cUrl);
      console.log(cI.name);
    }
  })();
});

function fCI (cUrl) {
  return new Promise((resolve, reject) => {
    request(cUrl, (charError, cR, charBody) => {
      if (charError) {

        reject(new Error(charError));
      } else if (cR.sC !== 200) {

        reject(new Error(`Unexpected response: ${cR.sC}`));
      } else {
        const cI = JSON.parse(charBody);
        resolve(cI);
      }
    });
  });
}
