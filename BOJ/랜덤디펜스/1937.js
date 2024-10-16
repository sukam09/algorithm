const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];
const OOB = (x, y) => x < 0 || x >= n || y < 0 || y >= n;

// dfs에서 시간초과가 나면 memoization을 시도해볼것 -> top-down dp
const dfs = (x, y) => {
  if (dp[x][y] !== 0) {
    return dp[x][y];
  }
  dp[x][y] = 1;
  for (let dir = 0; dir < 4; dir++) {
    const nx = x + dx[dir];
    const ny = y + dy[dir];
    if (OOB(nx, ny) || board[nx][ny] <= board[x][y]) {
      continue;
    }
    dp[x][y] = Math.max(dp[x][y], dfs(nx, ny) + 1);
  }
  return dp[x][y];
};

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input[0]);
const board = input.slice(1).map(x => x.split(' ').map(Number));
const dp = [...Array(n)].map(() => Array(n).fill(0));
let ans = 0;
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    ans = Math.max(ans, dfs(i, j));
  }
}
console.log(ans);
