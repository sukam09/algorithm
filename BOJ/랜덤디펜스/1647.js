const find = x => {
  if (p[x] < 0) {
    return x;
  }
  return (p[x] = find(p[x]));
};

const merge = (u, v) => {
  u = find(u);
  v = find(v);
  if (u === v) {
    return true;
  }
  if (p[u] === p[v]) {
    p[u]--;
  }
  if (p[u] < p[v]) {
    p[v] = u;
  } else {
    p[u] = v;
  }
  return false;
};

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = input[0].split(' ').map(Number)[0];
const edge = [];
for (let i = 1; i < input.length; i++) {
  const [a, b, c] = input[i].split(' ').map(Number);
  edge.push([c, a, b]);
}
edge.sort((a, b) => a[0] - b[0]);
const p = Array(n + 1).fill(-1);
let cnt = 0;
let ans = 0;
let mx = 0;
for (const [c, a, b] of edge) {
  if (cnt === n - 1) {
    break;
  }
  if (merge(a, b)) {
    continue;
  }
  ans += c;
  cnt++;
  mx = Math.max(mx, c);
}
console.log(ans - mx);
