class Queue {
  constructor() {
    this.dat = [];
    this.head = 0;
    this.tail = 0;
  }

  push(x) {
    this.dat[this.tail++] = x;
  }

  pop() {
    this.head++;
  }

  front() {
    return this.dat[this.head];
  }

  rear() {
    return this.dat[this.tail - 1];
  }

  empty() {
    return this.head === this.tail;
  }
}

const bfs = (sx, sy) => {
  const dist = [...Array(n)].map(() => Array(m).fill(-1));
  dist[sx][sy] = 0;
  const q = new Queue();
  q.push([sx, sy]);
  while (!q.empty()) {
    const [x, y] = q.front();
    q.pop();
    if (board[x][y] === "L" && dist[x][y] > 0) {
      ans = Math.max(ans, dist[x][y]);
    }
    for (let dir = 0; dir < 4; dir++) {
      const nx = x + dx[dir];
      const ny = y + dy[dir];
      if (OOB(nx, ny) || dist[nx][ny] !== -1 || board[nx][ny] === "W") {
        continue;
      }
      dist[nx][ny] = dist[x][y] + 1;
      q.push([nx, ny]);
    }
  }
};

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
const [n, m] = input[0].split(" ").map(Number);
const board = input.slice(1);
const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];
const OOB = (x, y) => x < 0 || x >= n || y < 0 || y >= m;
let ans = 0;
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (board[i][j] === "W") {
      continue;
    }
    bfs(i, j);
  }
}
console.log(ans);
