const left = (st, en) => (en - st + 10) % 10;

const solve = (i, k) => {
  if (i === n) {
    return 0;
  }
  if (dp[i][k] !== -1) {
    return dp[i][k];
  }
  const cur = (st[i] + k) % 10;
  const l = left(cur, en[i]);
  const r = 10 - l;
  const rotated = (k + l) % 10;
  return (dp[i][k] = Math.min(solve(i + 1, rotated) + l, solve(i + 1, k) + r));
};

const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const n = Number(input[0]);
const st = input[1].split("").map(Number);
const en = input[2].split("").map(Number);
const dp = [...Array(n)].map(() => Array(10).fill(-1));
solve(0, 0);
console.log(dp[0][0]);
