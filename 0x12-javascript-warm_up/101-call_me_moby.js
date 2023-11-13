#!/usr/bin/node

exports.callMeMoby = function (X, theFunction) {
  for (let i = 0; i < X; i++) {
    theFunction();
  }
};
