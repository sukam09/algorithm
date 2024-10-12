function solution(n, m, x, y, r, c, k) {
  // 1-index to 0-index
  x--; y--; r--; c--;

  // 사전 순: d, l, r, u
  const dx = [1, 0, 0, -1];
  const dy = [0, -1, 1, 0];
  const ds = 'dlru';

  const OOB = (x, y) => x < 0 || x >= n || y < 0 || y >= m;

  let ans = 'impossible';
  let found = 0;

  const dist = (a, b, c, d) => Math.abs(c - a) + Math.abs(d - b);

  const dfs = (x, y, s) => {
    if (found) {
      return;
    }

    const d = dist(x, y, r, c);
    const cnt = s.length;

    if (k - cnt < d || (k - cnt - d) % 2 === 1) {
      return;
    }

    if (s.length === k) {
      if (x === r && y === c) {
        ans = s;
        found = 1;
      }
      return;
    }

    if (x === r && y === c && (k - cnt) % 2 === 1) {
      return;
    }

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (OOB(nx, ny)) {
        continue;
      }
      dfs(nx, ny, s + ds[i]);
    }
  };

  dfs(x, y, '');

  return ans;
}
/*
가지치기(pruning)를 통해 DFS의 시간 복잡도를 획기적으로 줄일 수 있음
*/