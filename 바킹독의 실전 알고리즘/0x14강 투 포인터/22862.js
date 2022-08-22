const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number));

const [n, k] = input[0];
const arr = input[1];
let end = 0;

const oddBit = (x) => (x & 1 ? 1 : 0);
let oddNum = oddBit(arr[0]);
let evenNum = 1 - oddBit(arr[0]);
let answer = 0;

for (let start = 0; start < n; start++) {
  while (end + 1 < n && oddBit(arr[end + 1]) + oddNum <= k) {
    end++;
    oddNum += oddBit(arr[end]);
    evenNum += 1 - oddBit(arr[end]);
  }
  answer = Math.max(answer, evenNum);
  oddNum -= oddBit(arr[start]);
  evenNum -= 1 - oddBit(arr[start]);
}

console.log(answer);
