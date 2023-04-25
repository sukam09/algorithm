// hist 배열을 직접 구하는 방법 말고 노드가 독립집합에 속하는지를 체크하여 역추적하는 방법도 있음
const dfs = (v) => {
  dp[v][0] = 0;
  dp[v][1] = w[v];
  hist[v][1] = [v];
  for (const nv of adj[v]) {
    if (vis[nv]) {
      continue;
    }
    vis[nv] = true;
    dfs(nv);
    dp[v][0] += Math.max(...dp[nv]);
    dp[v][1] += dp[nv][0];
    if (dp[nv][0] >= dp[nv][1]) {
      hist[v][0].push(...hist[nv][0]);
    } else {
      hist[v][0].push(...hist[nv][1]);
    }
    hist[v][1].push(...hist[nv][0]);
  }
};

const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const n = Number(input[0]);
const w = [0, ...input[1].split(" ").map(Number)];
const adj = [...Array(n + 1)].map(() => []);
for (let i = 2; i < input.length; i++) {
  const [u, v] = input[i].split(" ").map(Number);
  adj[u].push(v);
  adj[v].push(u);
}
const dp = [...Array(n + 1)].map(() => Array(2).fill(0));
const vis = Array(n + 1).fill(false);
const hist = [...Array(n + 1)].map(() => [...Array(2)].map(() => []));
vis[1] = true;
dfs(1);
if (dp[1][0] >= dp[1][1]) {
  console.log(dp[1][0]);
  console.log(hist[1][0].sort((a, b) => a - b).join(" "));
} else {
  console.log(dp[1][1]);
  console.log(hist[1][1].sort((a, b) => a - b).join(" "));
}
