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

const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(x => x.split(' ').map(Number));

const dx = [1, 0, -1, 0, -1, -1, 1, 1];
const dy = [0, 1, 0, -1, -1, 1, -1, 1];
const OOB = (x, y) => x < 0 || x >= h || y < 0 || y >= w;

const solve = () => {
  let cnt = 0;
  const vis = Array(h)
    .fill()
    .map(() => Array(w).fill(false));
  const q = new Queue();
  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (vis[i][j] || board[i][j] === 0) {
        continue;
      }
      vis[i][j] = true;
      cnt++;
      q.push([i, j]);
      while (!q.empty()) {
        [x, y] = q.front();
        q.pop();
        for (let dir = 0; dir < 8; dir++) {
          const nx = x + dx[dir];
          const ny = y + dy[dir];
          if (OOB(nx, ny) || vis[nx][ny] || board[nx][ny] === 0) {
            continue;
          }
          vis[nx][ny] = true;
          q.push([nx, ny]);
        }
      }
    }
  }
  ans += `${cnt}\n`;
};

let chk = false;
let board;
let cnt = 0;
let w, h;
let ans = '';
for (let i = 0; i < input.length - 1; i++) {
  if (!chk) {
    [w, h] = input[i];
    board = [];
    chk = true;
  } else {
    cnt++;
    board.push(input[i]);
    if (cnt === h) {
      solve();
      cnt = 0;
      chk = false;
    }
  }
}
console.log(ans);
