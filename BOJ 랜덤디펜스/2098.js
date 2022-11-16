const dfs = (cur, vis) => {
  if (vis === (1 << n) - 1) {
    if (w[cur][0] === 0) {
      return Infinity;
    }
    return w[cur][0];
  }
  // dp 배열을 Infinity로 초기화하고 여기서 Infinity 기준으로 방문 여부를 판단하면 안되는 이유:
  // dp[cur][vis]가 방문했음에도 Infinity가 될 수 있어서?
  // memoization을 활용하지 못하므로 TLE
  if (dp[cur][vis] !== 0) {
    return dp[cur][vis];
  }
  dp[cur][vis] = Infinity;
  for (let i = 0; i < n; i++) {
    if (w[cur][i] === 0 || vis & (1 << i)) {
      continue;
    }
    dp[cur][vis] = Math.min(dp[cur][vis], dfs(i, vis | (1 << i)) + w[cur][i]);
  }
  return dp[cur][vis];
};

const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const n = Number(input[0]);
const w = input.slice(1).map((x) => x.split(" ").map(Number));
const dp = [...Array(n)].map(() => Array(1 << n).fill(0));
console.log(dfs(0, 1));
