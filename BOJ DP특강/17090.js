const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const [n, m] = input[0].split(' ').map(Number);
const board = input.slice(1);

const OOB = (x, y) => x < 0 || x >= n || y < 0 || y >= m;
const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];
const map = new Map();
map.set('D', 0);
map.set('R', 1);
map.set('U', 2);
map.set('L', 3);
const dp = Array(n)
  .fill()
  .map(() => Array(m).fill(-1));

const dfs = (x, y) => {
  if (OOB(x, y)) return 1;
  if (dp[x][y] !== -1) return dp[x][y];
  dp[x][y] = 0;
  const dir = map.get(board[x][y]);
  const nx = x + dx[dir];
  const ny = y + dy[dir];
  return (dp[x][y] = dfs(nx, ny));
};

let ans = 0;
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    ans += dfs(i, j);
  }
}
console.log(ans);
