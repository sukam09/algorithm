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

  isEmpty() {
    return this.head === this.tail;
  }
}

const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];
const OOB = (x, y) => x < 0 || x >= n || y < 0 || y >= n;

const bfs = (x, y) => {
  vis[x][y] = true;
  const q = new Queue();
  q.push([x, y]);
  let p = 0;
  let cnt = 0;
  const nxt = [];
  while (!q.isEmpty()) {
    const cur = q.front();
    q.pop();
    p += board[cur[0]][cur[1]];
    cnt++;
    nxt.push([cur[0], cur[1]]);
    for (let dir = 0; dir < 4; dir++) {
      const nx = cur[0] + dx[dir];
      const ny = cur[1] + dy[dir];
      if (OOB(nx, ny) || vis[nx][ny]) {
        continue;
      }
      const diff = Math.abs(board[nx][ny] - board[cur[0]][cur[1]]);
      if (diff >= l && diff <= r) {
        vis[nx][ny] = true;
        q.push([nx, ny]);
        chk = true;
      }
    }
  }
  for (const [x, y] of nxt) {
    board[x][y] = parseInt(p / cnt);
  }
};

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number));
const [n, l, r] = input[0];
const board = [];
for (let i = 1; i < input.length; i++) {
  board.push(input[i]);
}
const vis = Array(n);
for (let i = 0; i < n; i++) {
  vis[i] = Array(n).fill(false);
}
let ans = 0;
let chk;
while (true) {
  chk = false;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      vis[i][j] = false;
    }
  }
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (vis[i][j]) {
        continue;
      }
      bfs(i, j);
    }
  }
  if (!chk) {
    console.log(ans);
    break;
  }
  ans++;
}
