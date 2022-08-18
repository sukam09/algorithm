const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number));

const [n, k] = [input[0][0], input[0][1]];
const arr = input[1];
let answer = 0;
let end = 0;
const counter = Array(100001).fill(0);
counter[arr[0]] = 1;

for (let start = 0; start < n; start++) {
  while (end < n && counter[arr[end + 1]] < k) {
    end++;
    if (end < n) {
      counter[arr[end]]++;
    }
  }
  if (end === n) {
    break;
  }
  answer = Math.max(answer, end - start + 1);
  counter[arr[start]]--;
}

console.log(answer);
