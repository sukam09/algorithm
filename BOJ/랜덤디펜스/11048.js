const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(x => x.split(' ').map(Number));
const [n, m] = input[0];
const board = input.slice(1);
const d = Array(n)
  .fill()
  .map(() => Array(m).fill(0));
const OOB = (x, y) => x < 0 || x >= n || y < 0 || y >= m;
const dx = [-1, 0, -1];
const dy = [0, -1, -1];
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    let mx = 0;
    for (let k = 0; k < 3; k++) {
      const x = i + dx[k];
      const y = j + dy[k];
      if (OOB(x, y)) {
        continue;
      }
      mx = Math.max(mx, d[x][y]);
    }
    d[i][j] = mx + board[i][j];
  }
}
console.log(d[n - 1][m - 1]);
