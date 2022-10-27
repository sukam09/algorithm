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

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
const [r, c] = input[0].split(" ").map((x) => +x);
const board = input.slice(1);
const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];
const OOB = (x, y) => x < 0 || x >= r || y < 0 || y >= c;
const d1 = [...Array(r)].map(() => Array(c).fill(Infinity));
const q1 = new Queue();
const d2 = [...Array(r)].map(() => Array(c).fill(Infinity));
const q2 = new Queue();
let ex, ey; // 비버굴 위치
for (let i = 0; i < r; i++) {
  for (let j = 0; j < c; j++) {
    if (board[i][j] === "S") {
      d2[i][j] = 0;
      q2.push([i, j]);
    } else if (board[i][j] === "*") {
      d1[i][j] = 0;
      q1.push([i, j]);
    } else if (board[i][j] === "D") {
      ex = i;
      ey = j;
    }
  }
}
// 물 bfs
while (!q1.empty()) {
  const [x, y] = q1.front();
  q1.pop();
  for (let dir = 0; dir < 4; dir++) {
    const nx = x + dx[dir];
    const ny = y + dy[dir];
    if (
      OOB(nx, ny) ||
      d1[nx][ny] !== Infinity ||
      board[nx][ny] === "X" ||
      board[nx][ny] === "D"
    ) {
      continue;
    }
    d1[nx][ny] = d1[x][y] + 1;
    q1.push([nx, ny]);
  }
}
// 고슴도치 bfs
while (!q2.empty()) {
  const [x, y] = q2.front();
  q2.pop();
  if (x === ex && y === ey) {
    console.log(d2[x][y]);
    process.exit();
  }
  for (let dir = 0; dir < 4; dir++) {
    const nx = x + dx[dir];
    const ny = y + dy[dir];
    if (
      OOB(nx, ny) ||
      d2[nx][ny] !== Infinity ||
      board[nx][ny] === "X" ||
      d1[nx][ny] <= d2[x][y] + 1
    ) {
      continue;
    }
    d2[nx][ny] = d2[x][y] + 1;
    q2.push([nx, ny]);
  }
}
console.log("KAKTUS");
