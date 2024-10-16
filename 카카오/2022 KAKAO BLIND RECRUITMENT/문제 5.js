function solution(info, edges) {
  const n = info.length;
  const adj = [...Array(n)].map(() => []);
  for (const [a, b] of edges) {
    adj[a].push(b);
  }

  const vis = Array(1 << 17).fill(0);
  let ans = 0;

  const dfs = (state, cnt, wolf) => {
    if (wolf >= cnt - wolf) return;
    ans = Math.max(ans, cnt - wolf);

    for (let i = 0; i < n; i++) {
      if (!(state & (1 << i))) continue;
      for (let j = 0; j < adj[i].length; j++) {
        const nv = adj[i][j];
        const ns = state | (1 << nv);
        if (vis[ns]) continue;
        vis[ns] = 1;
        dfs(ns, cnt + 1, wolf + info[nv]);
      }
    }
  };

  vis[1] = 1;
  dfs(1, 1, 0);

  return ans;
}
