const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(x => x.split(' ').map(Number));
const n = input[0][0];
const a = input.slice(1, 1 + n);
let ans = '';
for (let idx = n + 2; idx < input.length; idx++) {
  let [i, j, x, y] = input[idx];
  i--;
  j--;
  x--;
  y--;
  let sum = 0;
  for (let r = i; r <= x; r++) {
    for (let c = j; c <= y; c++) {
      sum += a[r][c];
    }
  }
  ans += sum + '\n';
}
console.log(ans);
