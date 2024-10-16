const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = +input[0];
const arr = input[1].split(' ').map(v => +v);
const vis = Array(n).fill(0);
const arr2 = Array(n).fill(0);

const chk = () => {
  for (let num = 1; num <= n; num++) {
    let cnt = 0;
    for (let i = 0; i < n; i++) {
      if (arr2[i] === num) {
        break;
      }
      if (arr2[i] > num) {
        cnt++;
      }
    }
    if (cnt !== arr[num - 1]) {
      return 0;
    }
  }
  return 1;
};

const dfs = k => {
  if (k === n) {
    if (chk()) {
      console.log(arr2.join(' '));
    }
    return;
  }
  for (let i = 0; i < n; i++) {
    if (vis[i]) {
      continue;
    }
    vis[i] = 1;
    arr2[k] = i + 1;
    dfs(k + 1);
    vis[i] = 0;
  }
};

dfs(0);
