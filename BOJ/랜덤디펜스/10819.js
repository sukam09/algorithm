const dfs = (idx, val, hist) => {
  if (idx === n) {
    ans = Math.max(ans, val);
    return;
  }
  for (let i = 0; i < n; i++) {
    if (vis[i]) {
      continue;
    }
    vis[i] = true;
    if (idx > 0) {
      dfs(idx + 1, val + Math.abs(a[i] - hist[idx - 1]), [...hist, a[i]]);
    } else {
      dfs(idx + 1, val, [a[i]]);
    }
    vis[i] = false;
  }
};

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number));
const n = input[0][0];
const a = input[1];
let ans = 0;
const vis = Array(n).fill(false);
dfs(0, 0, []);
console.log(ans);
