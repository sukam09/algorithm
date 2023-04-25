const [n, m] = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split(' ').map(Number);
const arr = Array(m).fill(0);
let ans = '';

const dfs = k => {
  if (k === m) {
    ans += arr.join(' ') + '\n';
    return;
  }
  let st = 1;
  if (k > 0) st = arr[k - 1];
  for (let i = st; i <= n; i++) {
    arr[k] = i;
    dfs(k + 1);
  }
};

dfs(0);
console.log(ans);
