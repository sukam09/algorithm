const move = (st, en) => {
  if (st === 0) {
    return 2;
  }
  if (st === en) {
    return 1;
  }
  if (Math.abs(st - en) === 2) {
    return 4;
  }
  return 3;
};

const solve = (cur, l, r) => {
  if (cur === n) {
    return 0;
  }
  if (dp[cur][l][r] !== Infinity) {
    return dp[cur][l][r];
  }
  // 아래 조건을 체크하지 않아도 AC를 받을 수 있음
  // Why??
  // if (i !== 0 && l === r) {
  //   return Infinity;
  // }
  const nxt = arr[cur];
  return (dp[cur][l][r] = Math.min(
    dp[cur][l][r],
    solve(cur + 1, nxt, r) + move(l, nxt),
    solve(cur + 1, l, nxt) + move(r, nxt)
  ));
};

const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const arr = input[0].split(" ").map(Number);
arr.pop();
const n = arr.length;
const dp = [...Array(n)].map(() =>
  [...Array(5)].map(() => Array(5).fill(Infinity))
);
console.log(solve(0, 0, 0));
