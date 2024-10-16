const dfs = v => {
  for (const nv of adj[v]) {
    if (nv === p[v]) {
      continue;
    }
    p[nv] = v;
    depth[nv] = depth[v] + 1;
    dfs(nv);
  }
};

// u, v 노드를 같은 depth까지 끌어올린 후, 동시에 두 노드를 올리면서 같아지는 노드가 LCA가 된다.
const solve = (u, v) => {
  if (depth[u] < depth[v]) {
    [u, v] = [v, u];
  }
  while (depth[u] !== depth[v]) {
    u = p[u];
  }
  while (u !== v) {
    u = p[u];
    v = p[v];
  }
  ans += u + '\n';
};

const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const n = Number(input[0]);
const adj = [...Array(n + 1)].map(() => []);
for (let i = 1; i < n; i++) {
  const [u, v] = input[i].split(' ').map(Number);
  adj[u].push(v);
  adj[v].push(u);
}
const p = Array(n + 1).fill(0);
const depth = Array(n + 1).fill(0);
dfs(1);
let ans = '';
for (let i = n + 1; i < input.length; i++) {
  const [u, v] = input[i].split(' ').map(Number);
  solve(u, v);
}
console.log(ans);
