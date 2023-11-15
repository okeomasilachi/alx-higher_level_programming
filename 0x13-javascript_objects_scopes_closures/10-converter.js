#!/usr/bin/node

exports.converter = function (number, base) {
    return Array.from({ length: number + 1 }, (_, i) =>
      (i ? (number % base ** i / base ** (i - 1)) | 0 : number % base).toString(base)
    ).reverse().join('');
  };
  