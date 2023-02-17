// 입력(fs를 이용한 방식)
const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');

// 입력(readline을 이용한 방식)
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];
rl.on('line', x => {
  input.push(x);
}).on('close', () => {
  console.log(input);
  process.exit();
});

// 큐
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

// 최소 힙
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
      if (this.dat[par] <= this.dat[idx]) {
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
      if (rc <= this.sz && this.dat[rc] < this.dat[lc]) {
        mc = rc;
      }
      if (this.dat[idx] <= this.dat[mc]) {
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

// 최대 힙
class MaxHeap {
  constructor() {
    this.dat = [];
    this.sz = 0;
  }

  push(x) {
    this.dat[++this.sz] = x;
    let idx = this.sz;
    while (idx > 1) {
      const par = Math.floor(idx / 2);
      if (this.dat[par] >= this.dat[idx]) {
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
      if (rc <= this.sz && this.dat[rc] > this.dat[lc]) {
        mc = rc;
      }
      if (this.dat[idx] >= this.dat[mc]) {
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

// 다익스트라
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

// 순열
// 예시. BOJ 15649번: N과 M (1)
const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const [n, m] = input[0].split(' ').map(Number);
const arr = Array(m).fill(0);
const vis = Array(m).fill(false);
let ans = '';

const dfs = k => {
  if (k === m) {
    ans += arr.join(' ') + '\n';
    return;
  }
  for (let i = 1; i <= n; i++) {
    if (vis[i]) {
      continue;
    }
    vis[i] = true;
    arr[k] = i;
    dfs(k + 1);
    vis[i] = false;
  }
};

dfs(0);
console.log(ans);

// 조합
// 예시. BOJ 15650번: N과 M (2)
const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const [n, m] = input[0].split(' ').map(Number);
const arr = Array(m).fill(0);
const vis = Array(m).fill(false);
let ans = '';

const dfs = k => {
  if (k === m) {
    ans += arr.join(' ') + '\n';
    return;
  }
  let st = 1;
  if (k > 0) {
    st = arr[k - 1] + 1;
  }
  for (let i = st; i <= n; i++) {
    if (vis[i]) {
      continue;
    }
    vis[i] = true;
    arr[k] = i;
    dfs(k + 1);
    vis[i] = false;
  }
};

dfs(0);
console.log(ans);
