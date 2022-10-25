const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number));
const k = input[0][1];
const a = input[1];
a.sort((a, b) => a - b);
console.log(a[k - 1]);
