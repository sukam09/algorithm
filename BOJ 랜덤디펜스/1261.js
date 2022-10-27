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
const [m, n] = input[0].split(" ").map((x) => +x); // n, m이 아님에 주의
const board = input.slice(1).map((x) => x.split("").map((x) => +x));
const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];
const OOB = (x, y) => x < 0 || x >= n || y < 0 || y >= m;
const dist = [...Array(n)].map(() => Array(m).fill(Infinity));
const q = new Queue();
dist[0][0] = 0;
q.push([0, 0]);
while (!q.empty()) {
  const [x, y] = q.front();
  q.pop();
  for (let dir = 0; dir < 4; dir++) {
    const nx = x + dx[dir];
    const ny = y + dy[dir];
    if (OOB(nx, ny) || dist[x][y] + board[nx][ny] >= dist[nx][ny]) {
      continue;
    }
    dist[nx][ny] = dist[x][y] + board[nx][ny];
    q.push([nx, ny]);
  }
}
console.log(dist[n - 1][m - 1]);
/*
Note.
다음과 같이 전처리할 경우 m, n 중 하나가 두 자리 수인 경우 잘못된 값이 들어갈 수 있음
따라서 앞으로 이와 같은 전처리 방법은 사용하지 않도록 함
map으로 한꺼번에 전처리하는 대신 한 줄씩 읽으면서 그때 그때 하는 방식으로 변경

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split("").map((x) => +x));
const [m, n] = [input[0][0], input[0][2]];
*/
