const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number));
const n = input[0][0];
const d = Array(n + 1)
  .fill()
  .map(() => Array(3).fill(1));
for (let i = 2; i <= n; i++) {
  d[i][0] = d[i - 1].reduce((a, b) => a + b, 0) % 9901;
  d[i][1] = (d[i - 1][0] + d[i - 1][2]) % 9901;
  d[i][2] = (d[i - 1][0] + d[i - 1][1]) % 9901;
}
let ans = d[n].reduce((a, b) => a + b, 0) % 9901;
console.log(ans);
