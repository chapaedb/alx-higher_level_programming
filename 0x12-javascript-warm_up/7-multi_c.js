#!/usr/bin/node

let args = process.argv[2];
let num = parseInt(args);

if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    console.log("C is fun");
  }
} else {
  console.log("Missing number of occurrences");
}
