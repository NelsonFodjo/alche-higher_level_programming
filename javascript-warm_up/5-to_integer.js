#!/usr/bin/node
const num = process.argv[2];

if (num.int === Number) {
console.log(`My number: ${num.int}`); }
else{
    console.log("Not a number");
}