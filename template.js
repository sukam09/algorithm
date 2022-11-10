// 입력
const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");

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

const dijkstra = (st) => {
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

// 아래는 추후 추가 예정
// 순열

// 조합
