const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const k = Number(input[0]);
const w = input[1].split(' ').map(Number);
const n = Math.pow(2, k + 1) - 1;
const lc = Array(n + 1).fill(0);
const rc = Array(n + 1).fill(0);
let ans = 0;
for (let i = 0; i < w.length / 2; i++) {
  lc[i + 1] = w[i * 2];
  rc[i + 1] = w[i * 2 + 1];
  ans += lc[i + 1] + rc[i + 1];
}

let mx = 0;
const d = Array(n + 1).fill(0);

const dfs = (cur, val) => {
  if (lc[cur] === 0) {
    d[cur] = val;
    mx = Math.max(mx, val);
    return;
  }
  const l = cur * 2;
  const r = cur * 2 + 1;
  dfs(l, val + lc[cur]);
  dfs(r, val + rc[cur]);
};

dfs(1, 0);
const st = Math.pow(2, k);
for (let i = st; i <= n; i++) {
  d[i] = mx - d[i];
}

const solve = cur => {
  if (cur >= st) return;
  const l = cur * 2;
  const r = cur * 2 + 1;
  solve(l);
  solve(r);
  const mn = Math.min(d[l], d[r]);
  d[l] -= mn;
  d[r] -= mn;
  d[cur] += mn;
};
solve(1);
for (let i = 1; i <= n; i++) ans += d[i];
console.log(ans);
