#!/usr/bin/node

function findSecondBiggest(numbers) {
  if (numbers.length <= 1) {
    return 0;
  }

  let max = Number.MIN_SAFE_INTEGER;
  let secondMax = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < numbers.length; i++) {
    let num = parseInt(numbers[i]);
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num < max) {
      secondMax = num;
    }
  }

  return secondMax;
}

let args = process.argv.slice(2);
console.log(findSecondBiggest(args));
