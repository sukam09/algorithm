/*
A1 = M * q1 + r1
A2 = M * q2 + r2
A1 - A2 = M * (q1 - q2) + (r1 - r2)
        = M * (q1 - q2) (∵ r1 = r2)
마찬가지로, A3 - A2 = M * (q3 - q2)
따라서, M은 Ai+1 - Ai(1 <= i < n)의 공약수
*/
const gcd = (a, b) => {
  if (b > a) {
    [a, b] = [b, a];
  }
  if (b === 0) {
    return a;
  }
  return gcd(b, a % b);
};

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input[0]);
const arr = input.slice(1).map(Number);
arr.sort((a, b) => a - b);
let gcdval = arr[1] - arr[0];
for (let i = 1; i < n - 1; i++) {
  gcdval = gcd(gcdval, arr[i + 1] - arr[i]);
}
let ans = '';
for (let i = 2; i <= gcdval; i++) {
  if (gcdval % i === 0) {
    ans += i + ' ';
  }
}
console.log(ans);
