const dfs = (idx, hist) => {
  if (idx === n) {
    ans += `${hist.join(" ")}\n`;
    return;
  }
  for (let i = 1; i <= n; i++) {
    if (vis[i]) {
      continue;
    }
    vis[i] = true;
    dfs(idx + 1, [...hist, i]);
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
const vis = Array(n + 1).fill(false);
let ans = "";
dfs(0, []);
console.log(ans);
