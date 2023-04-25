const [n, m] = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split(' ').map(Number);
const vis = Array(n + 1).fill(0);
const arr = Array(m).fill(0);
let ans = '';

const dfs = k => {
  if (k === m) {
    ans += arr.join(' ') + '\n';
    return;
  }
  let st = 1;
  if (k > 0) st = arr[k - 1] + 1;
  for (let i = st; i <= n; i++) {
    if (vis[i]) continue;
    vis[i] = 1;
    arr[k] = i;
    dfs(k + 1);
    vis[i] = 0;
  }
};
dfs(0);
console.log(ans);
