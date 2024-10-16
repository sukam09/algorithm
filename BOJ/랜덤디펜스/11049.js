const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input[0]);
const arr = input.slice(1).map(x => x.split(' ').map(Number));

// chained matrix multiplication algorithm
// BOJ 11066번: 파일 합치기랑 비슷한 문제
const dp = [...Array(n)].map(() => Array(n).fill(Infinity));
for (let d = 0; d < n; d++) {
  for (let i = 0; i < n - d; i++) {
    const j = i + d;
    if (i === j) {
      dp[i][j] = 0;
      continue;
    }
    for (let k = i; k < j; k++) {
      dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k + 1][j] + arr[i][0] * arr[k][1] * arr[j][1]);
    }
  }
}
console.log(dp[0][n - 1]);
