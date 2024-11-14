#!/usr/bin/node
const request = require('request');

const link = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
async function _helper (link) {
  return new Promise((resolve, reject) => {
    request(link, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      resolve(JSON.parse(body));
    });
  });
}
request(link, async (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  for (const link of data.characters) {
    try {
      const person = await _helper(link);
      console.log(person.name);
    } catch (err) {
      console.error(err);
    }
  }
});
