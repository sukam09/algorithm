class MinHeap {
  constructor() {
    this.dat = [];
    this.sz = 0;
  }

  push(x) {
    this.dat[++this.sz] = x;
    let idx = this.sz;
    while (idx > 1) {
      const par = Math.floor(idx / 2);
      if (this.dat[par][0] <= this.dat[idx][0]) {
        break;
      }
      this.swap(par, idx);
      idx = par;
    }
  }

  top() {
    return this.dat[1];
  }

  pop() {
    this.dat[1] = this.dat[this.sz--];
    let idx = 1;
    while (2 * idx <= this.sz) {
      const lc = 2 * idx;
      const rc = 2 * idx + 1;
      let mc = lc;
      if (rc <= this.sz && this.dat[rc][0] < this.dat[lc][0]) {
        mc = rc;
      }
      if (this.dat[idx][0] <= this.dat[mc][0]) {
        break;
      }
      this.swap(idx, mc);
      idx = mc;
    }
  }

  swap(a, b) {
    [this.dat[a], this.dat[b]] = [this.dat[b], this.dat[a]];
  }

  empty() {
    return this.sz === 0;
  }
}

const dijkstra = st => {
  dist[st] = 0;
  const pq = new MinHeap();
  pq.push([dist[st], st]);
  while (!pq.empty()) {
    const [d, v] = pq.top();
    pq.pop();
    if (dist[v] !== d) {
      continue;
    }
    for (const [nd, nv] of adj[v]) {
      if (dist[nv] <= dist[v] + nd) {
        continue;
      }
      dist[nv] = dist[v] + nd;
      pq.push([dist[nv], nv]);
    }
  }
};

const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];
const OOB = (x, y) => x < 0 || x >= n || y < 0 || y >= n;

// x * 5 + y를 정점으로 가지고 도둑루피 수를 가중치로 가지는 그래프로 변경 -> dijkstra
// dp로는 못푸는 이유..?
const solve = () => {
  adj = [...Array(n * n)].map(() => []);
  for (let i = 0; i < n * n; i++) {
    for (let dir = 0; dir < 4; dir++) {
      const x = parseInt(i / n);
      const y = i % n;
      const nx = x + dx[dir];
      const ny = y + dy[dir];
      if (OOB(nx, ny)) {
        continue;
      }
      const idx = nx * n + ny;
      adj[i].push([board[nx][ny], idx]);
    }
  }
  dist = Array(n * n).fill(Infinity);
  dijkstra(0);
  ans += `Problem ${tc}: ${dist[n * n - 1] + board[0][0]}\n`;
};

const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
let chk = false;
let n;
let board;
let ans = '';
let tc = 0;
let cnt;
let dist;
let adj;
for (let i = 0; i < input.length; i++) {
  if (!chk) {
    if (i !== 0) {
      solve(++tc);
    }
    n = Number(input[i]);
    board = [];
    chk = true;
    cnt = 0;
  } else {
    board.push(input[i].split(' ').map(Number));
    if (++cnt === n) {
      chk = false;
    }
  }
}
console.log(ans);
