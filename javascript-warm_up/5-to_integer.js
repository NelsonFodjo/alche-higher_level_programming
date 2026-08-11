#!/usr/bin/node
const num = process.argv[2];

if (parseInt(num, 10) === Number) {
console.log(`My number: ${parseInt(num, 10)}`); }
else{
    console.log("Not a number");
}