const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const n = Number(input[0]);
const a = input[1].split(' ').map(Number);
const m = Number(input[2]);
const d = Array(4)
  .fill()
  .map(() => Array(n + 1).fill(0));
const s = Array(n + 1).fill(0);
s[1] = a[0];
for (let i = 2; i <= n; i++) {
  s[i] = s[i - 1] + a[i - 1];
}
for (let i = 1; i <= 3; i++) {
  for (let j = i * m; j <= n; j++) {
    d[i][j] = Math.max(d[i][j - 1], d[i - 1][j - m] + s[j] - s[j - m]);
  }
}
console.log(d[3][n]);
