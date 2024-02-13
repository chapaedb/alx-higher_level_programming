#!/usr/bin/node

let args = process.argv[2];
let size = parseInt(args);

if (!isNaN(size)) {
  if (size <= 0) {
    console.log("Size must be a positive number");
  } else {
    for (let i = 0; i < size; i++) {
      let line = "";
      for (let j = 0; j < size; j++) {
        line += "X";
      }
      console.log(line);
    }
  }
} else {
  console.log("Missing size");
}
