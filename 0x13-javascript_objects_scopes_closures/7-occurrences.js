#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;

  if (list && searchElement) {
    for (let j = 0; j < list.length; j++) {
      if (list[j] === searchElement) {
        i++;
      }
    }
    return (i);
  }
};
