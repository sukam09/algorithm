const dfs = (v) => {
  for (const nv of adj[v]) {
    if (vis[nv]) {
      cnt++;
      return;
    }
    vis[nv] = true;
    dfs(nv);
  }
};

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
let cnt;
let vis;
let ans = "";
let adj;
for (let i = 1; i < input.length; i += 2) {
  const n = Number(input[i]);
  const arr = input[i + 1].split(" ").map(Number);
  adj = [...Array(n + 1)].map(() => []);
  for (let j = 0; j < arr.length; j++) {
    adj[j + 1].push(arr[j]);
  }
  cnt = 0;
  vis = Array(n + 1).fill(false);
  for (let i = 1; i <= n; i++) {
    if (vis[i]) {
      continue;
    }
    vis[i] = true;
    dfs(i);
  }
  ans += cnt + "\n";
}
console.log(ans);
