function solution(board, skill) {
  const n = board.length;
  const m = board[0].length;
  
  const d = [...Array(n + 1)].map(() => Array(m + 1).fill(0));
  for (let [type, r1, c1, r2, c2, degree] of skill) {
    if (type === 1) degree = -degree;
    d[r1][c1] += degree;
    d[r1][c2 + 1] -= degree;
    d[r2 + 1][c1] -= degree;
    d[r2 + 1][c2 + 1] += degree;
  }
  
  for (let i = 1; i < n; i++) {
    for (let j = 0; j < m; j++) {
      d[i][j] += d[i - 1][j];
    }
  }
  
  for (let i = 0; i < n; i++) {
    for (let j = 1; j < m; j++) {
      d[i][j] += d[i][j - 1];
    }
  }
  
  let ans = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j] + d[i][j] > 0) ans++;
    }
  }
  
  return ans;
}
/*
imos법 (いもす法, imos法)
*/