const [n, m] = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split(' ').map(Number);
const arr = Array(m).fill(0);
let ans = '';

const dfs = k => {
  if (k === m) {
    ans += arr.join(' ') + '\n';
    return;
  }
  for (let i = 1; i <= n; i++) {
    arr[k] = i;
    dfs(k + 1);
  }
};

dfs(0);
console.log(ans);
