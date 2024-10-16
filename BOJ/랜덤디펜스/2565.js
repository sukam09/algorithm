const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(x => x.split(' ').map(Number));
const n = input[0][0];
const a = input.slice(1);
a.sort((a, b) => a[0] - b[0]);
const b = a.map(x => x[1]);
let mx = 0;
const d = Array(n).fill(1);
for (let i = 0; i < b.length; i++) {
  for (let j = 0; j < i; j++) {
    if (b[i] > b[j]) {
      d[i] = Math.max(d[i], d[j] + 1);
      mx = Math.max(mx, d[i]);
    }
  }
}
console.log(n - mx);
