const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const [n, m] = [input[0].length, input[1].length];
const [a, b] = [input[0], input[1]];
const dp = [...Array(n + 1)].map(() => Array(m + 1).fill(""));
for (let i = 1; i <= n; i++) {
  for (let j = 1; j <= m; j++) {
    if (a[i - 1] === b[j - 1]) {
      dp[i][j] = dp[i - 1][j - 1] + a[i - 1];
    } else {
      const x = dp[i - 1][j].length;
      const y = dp[i][j - 1].length;
      dp[i][j] = x >= y ? dp[i - 1][j] : dp[i][j - 1];
    }
  }
}
console.log(dp[n][m].length);
if (dp[n][m] !== "") {
  console.log(dp[n][m]);
}
