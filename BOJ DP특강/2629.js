const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const [n, m] = [Number(input[0]), Number(input[2])];
const w = input[1].split(' ').map(Number);
const b = input[3].split(' ').map(Number);
let ws = 0;
for (let i = 0; i < n; i++) ws += w[i];
const d = Array(n + 1)
  .fill()
  .map(() => Array(ws + 1).fill(0));

const solve = (i, j) => {
  if (i > n || d[i][j]) return;
  d[i][j] = 1;
  solve(i + 1, j);
  solve(i + 1, j + w[i]);
  solve(i + 1, Math.abs(j - w[i]));
};

solve(0, 0);
let ans = '';
for (let i = 0; i < m; i++) {
  const x = b[i];
  if (x > 15000) ans += 'N ';
  else if (d[n][x]) ans += 'Y ';
  else ans += 'N ';
}
console.log(ans);
