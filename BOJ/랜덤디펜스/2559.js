const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, k] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);
let sum = arr.slice(0, k).reduce((a, b) => a + b, 0);
let ans = sum;
for (let i = 1; i <= n - k; i++) {
  sum -= arr[i - 1];
  sum += arr[i + k - 1];
  ans = Math.max(ans, sum);
}
console.log(ans);
