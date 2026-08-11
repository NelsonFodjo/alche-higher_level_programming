#!/usr/bin/node
num = parseInt(process.argv[2], 10);

function factorial (num) {
  if (num == 1) {
    return num;
  } else {
    return num * factorial(num - 1);
  }
}

if (isNaN) {
  console.log('1');
} else {
  console.log(factorial(num));
}
