const find = x => {
  if (p[x] < 0) return x;
  return (p[x] = find(p[x]));
};

const isDiffGroup = (u, v) => {
  u = find(u);
  v = find(v);
  if (u === v) {
    return false;
  }
  if (p[u] === p[v]) {
    p[u]--;
  }
  if (p[u] < p[v]) {
    p[v] = u;
  } else {
    p[u] = v;
  }
  return true;
};

const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(x => x.split(' ').map(Number));
console.log(input);
const [n, m] = [input[0][0], input[1][0]];
const edge = input.slice(2);
const p = Array(n + 1).fill(-1);
let ans = 0;
// 크루스칼 알고리즘
edge.sort((a, b) => a[2] - b[2]);
let cnt = 0;
for (let i = 0; i < edge.length; i++) {
  const [a, b, c] = edge[i];
  if (!isDiffGroup(a, b)) {
    continue;
  }
  ans += c;
  cnt++;
  if (cnt == n - 1) {
    break;
  }
}
console.log(ans);
