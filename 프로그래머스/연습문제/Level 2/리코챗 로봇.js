const OOB = (x, y) => x < 0 || x >= n || y < 0 || y >= m;
const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];
let n, m;
let ans = Infinity;
let gx, gy;
let board_;
let dist;
let possible = 0;

const move = (x, y, d) => {
  let cx, cy;
  cx = x;
  cy = y;
  while (1) {
    const nx = cx + dx[d];
    const ny = cy + dy[d];
    if (OOB(nx, ny) || board_[nx][ny] === 'D') {
      return [cx, cy];
    }
    cx = nx;
    cy = ny;
  }
};

const dfs = (x, y, cur) => {
  if (x === gx && y === gy) {
    ans = Math.min(ans, cur);
    possible = 1;
    return;
  }
  for (let d = 0; d < 4; d++) {
    const [nx, ny] = move(x, y, d);
    if (dist[nx][ny] !== -1 && dist[nx][ny] <= cur) continue;
    dist[nx][ny] = cur;
    dfs(nx, ny, cur + 1);
  }
};

function solution(board) {
  board_ = board;
  n = board.length;
  m = board[0].length;
  let rx, ry;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j] === 'R') {
        rx = i;
        ry = j;
      } else if (board[i][j] === 'G') {
        gx = i;
        gy = j;
      }
    }
  }
  dist = Array(n)
    .fill()
    .map(() => Array(m).fill(-1));
  dist[rx][ry] = 0;
  dfs(rx, ry, 0);
  if (!possible) ans = -1;
  return ans;
}
