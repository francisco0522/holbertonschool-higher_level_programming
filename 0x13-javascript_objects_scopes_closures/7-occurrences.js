#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numOcc = 0;
  for (let i = 0; i <= list.length; i++) {
    if (list[i] === searchElement) {
      numOcc = numOcc + 1;
    }
  }
  return (numOcc);
};
