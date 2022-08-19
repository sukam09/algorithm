const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number));

const n = input[0][0];
const arr = input[1];

let answer = 0;
let end = 0;
const checker = Array(100001).fill(false);
checker[arr[0]] = true;

for (let start = 0; start < n; start++) {
  while (end + 1 < n && !checker[arr[end + 1]]) {
    checker[arr[++end]] = true;
  }
  answer += end - start + 1;
  checker[arr[start]] = false;
}

console.log(answer);
