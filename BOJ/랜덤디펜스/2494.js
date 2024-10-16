const left = (st, en) => (en - st + 10) % 10;

const solve = (i, k) => {
  if (i === n) {
    return 0;
  }
  if (dp[i][k] !== -1) {
    return dp[i][k];
  }
  const cur = (st[i] + k) % 10;
  const l = left(cur, en[i]);
  const r = 10 - l;
  const rotated = (k + l) % 10;
  const tl = solve(i + 1, rotated) + l;
  const tr = solve(i + 1, k) + r;
  if (tl <= tr) {
    hist[i][k] = l;
  } else {
    hist[i][k] = -r;
  }
  return (dp[i][k] = Math.min(tl, tr));
};

const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const n = Number(input[0]);
const st = input[1].split('').map(Number);
const en = input[2].split('').map(Number);
const dp = [...Array(n)].map(() => Array(10).fill(-1));
const hist = [...Array(n)].map(() => Array(10).fill(0));
solve(0, 0);
const cnt = dp[0][0];
let route = '';
let k = 0;
for (let i = 0; i < n; i++) {
  if (hist[i][k] === 0) {
    continue;
  }
  route += `${i + 1} ${hist[i][k]}\n`;
  if (hist[i][k] > 0) {
    k = (k + hist[i][k]) % 10;
  }
}
console.log(cnt);
console.log(route);
