const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const n = input[0];
const arr = [];
for (let i = 1; i <= n; i++) {
  arr.push(input[i]);
}
arr.sort((a, b) => a - b);

const pairs = [];
for (let i = 0; i < n; i++) {
  for (let j = i; j < n; j++) {
    pairs.push(arr[i] + arr[j]);
  }
}
pairs.sort((a, b) => a - b);

const solution = (target) => {
  let start = 0;
  let end = pairs.length - 1;
  while (start <= end) {
    const mid = Math.floor((start + end) / 2);
    // 여기서 모든 경우의 수를 다 처리해 줘야함
    // start와 end가 같아지는 경우까지 고려할 것
    if (pairs[mid] === target) {
      return true;
    }
    if (target < pairs[mid]) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return false;
};

for (let i = n - 1; i >= 0; i--) {
  for (let j = 0; j < i; j++) {
    const target = arr[i] - arr[j];
    if (solution(target)) {
      console.log(arr[i]);
      process.exit(0);
    }
  }
}
