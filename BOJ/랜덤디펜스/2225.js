const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number));
const [n, k] = input[0];
const d = Array(k + 1);
for (let i = 0; i <= k; i++) {
  d[i] = Array(n + 1).fill(0);
}
for (let j = 0; j <= n; j++) {
  d[1][j] = 1;
}
for (let i = 2; i <= k; i++) {
  for (let j = 0; j <= n; j++) {
    for (let l = 0; l <= j; l++) {
      d[i][j] += d[i - 1][l] % 1000000000;
      d[i][j] %= 1000000000;
    }
  }
}
// console.log(d);
console.log(d[k][n]);
