function solution(edges) {
  const MX = 1000001;

  const adj = [...Array(MX)].map(() => []);
  const indegree = Array(MX).fill(0);
  const outdegree = Array(MX).fill(0);
  let st = 0;

  for (const [a, b] of edges) {
    adj[a].push(b);
    outdegree[a]++;
    indegree[b]++;
  }

  for (let i = 1; i <= 1000000; i++) {
    if (indegree[i] === 0 && outdegree[i] >= 2) {
      st = i;
      break;
    }
  }

  const ret = [0, 0, 0]; // 막대, 도넛, 8자
  let cur = 0; // 그래프 종류: 0, 1, 2 -> 막대, 도넛, 8자
  const vis = Array(MX).fill(0);
  let stk = [];

  const dfs = () => {
    while (stk.length > 0) {
      const v = stk.pop();

      if (indegree[v] >= 2 && outdegree[v] === 2) {
        cur = 2;
        return;
      }

      for (const nv of adj[v]) {
        if (vis[nv]) {
          cur = 1;
          return;
        }
        vis[nv] = 1;
        stk.push(nv);
      }
    }
  };

  for (const tg of adj[st]) {
    vis[tg] = 1;
    stk = [tg];
    cur = 0;
    dfs();
    ret[cur]++;
  }

  return [st, ret[1], ret[0], ret[2]];
}
/*
dfs를 재귀 방식으로 할 경우 터짐
*/
