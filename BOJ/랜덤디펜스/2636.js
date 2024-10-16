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

const solve = () => {
  const vis = [...Array(n)].map(() => Array(m).fill(false));
  vis[0][0] = true;
  const q = new Queue();
  q.push([0, 0]);
  while (!q.empty()) {
    const [x, y] = q.front();
    q.pop();
    for (let dir = 0; dir < 4; dir++) {
      const nx = x + dx[dir];
      const ny = y + dy[dir];
      if (OOB(nx, ny) || vis[nx][ny]) {
        continue;
      }
      vis[nx][ny] = true;
      if (board[nx][ny] === 1) {
        cnt--;
        board[nx][ny] = 0;
      } else {
        q.push([nx, ny]);
      }
    }
  }
};

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m] = input[0].split(' ').map(Number);
const board = input.slice(1).map(x => x.split(' ').map(Number));
const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];
const OOB = (x, y) => x < 0 || x >= n || y < 0 || y >= m;
let cnt = 0;
board.forEach(x => {
  cnt += x.filter(y => y === 1).length;
});
let ans1 = 0;
let ans2 = cnt;
while (true) {
  if (cnt === 0) {
    break;
  }
  ans1++;
  ans2 = cnt;
  solve();
}
console.log(`${ans1}\n${ans2}`);
