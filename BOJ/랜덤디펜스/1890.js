// 정답 범위가 최대 2^63-1이므로 BigInt를 사용
const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map((x) => +x));

const n = input[0][0];
const a = input.slice(1);
const d = Array(n)
  .fill()
  .map(() => Array(n).fill(0n));
d[0][0] = 1n;
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    const step = a[i][j];
    if (step === 0) {
      continue;
    }
    if (i + step < n) {
      d[i + step][j] += d[i][j];
    }
    if (j + step < n) {
      d[i][j + step] += d[i][j];
    }
  }
}
console.log(d[n - 1][n - 1].toString());
