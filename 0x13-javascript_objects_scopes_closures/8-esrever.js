#!/usr/bin/node

exports.esrever = function (list) {
  if (list) {
    const N = [];
    let k = 0;

    for (let i = list.length; i > -1; i--) {
      if (list[i] !== undefined && i !== undefined) {
        N[k++] = list[i];
      }
    }
    return (N);
  }
};
