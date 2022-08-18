const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number));

const [n, d, k, c] = input[0];
const arr = [];
const checker = new Map();
checker.set(c, 1);

for (let i = 1; i <= n; i++) {
  arr.push(input[i][0]);
}
for (let i = 1; i <= k - 1; i++) {
  arr.push(input[i][0]);
}

for (let i = 0; i < k; i++) {
  if (checker.has(arr[i])) {
    checker.set(arr[i], checker.get(arr[i]) + 1);
  } else {
    checker.set(arr[i], 1);
  }
}

let answer = checker.size;
for (let start = 1; start < n; start++) {
  const end = start + k - 1;
  checker.set(arr[start - 1], checker.get(arr[start - 1]) - 1);
  if (checker.get(arr[start - 1]) === 0) {
    checker.delete(arr[start - 1]);
  }
  if (checker.has(arr[end])) {
    checker.set(arr[end], checker.get(arr[end]) + 1);
  } else {
    checker.set(arr[end], 1);
  }
  answer = Math.max(answer, checker.size);
}
console.log(answer);
