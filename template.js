// 입력
const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
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
      const p = Math.floor(idx / 2);
      if (this.dat[p] <= this.dat[idx]) {
        break;
      }
      this.swap(p, idx);
      idx = p;
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

  isEmpty() {
    return this.sz === 0;
  }
}

// 최대 힙
class MaxHeap {
  constructor() {
    this.dat = [];
    this.sz = 0;
  }

  push(item) {
    this.dat[++this.sz] = item;
    let idx = this.sz;
    while (idx > 1) {
      const p = Math.floor(idx / 2);
      if (this.dat[p] >= this.dat[idx]) {
        break;
      }
      this.swap(p, idx);
      idx = p;
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

  isEmpty() {
    return this.sz === 0;
  }
}

// 다익스트라
class MinHeap {
  constructor() {
    this.heap = [];
    this.sz = 0;
  }

  push(item) {
    this.heap[++this.sz] = item;
    let idx = this.sz;
    while (idx > 1) {
      const p = Math.floor(idx / 2);
      if (this.heap[p][0] <= this.heap[idx][0]) {
        break;
      }
      this.swap(p, idx);
      idx = p;
    }
  }

  pop() {
    const item = this.heap[1];
    this.heap[1] = this.heap[this.sz--];
    let idx = 1;
    while (2 * idx <= this.sz) {
      const lc = 2 * idx;
      const rc = 2 * idx + 1;
      let mc = lc;
      if (rc <= this.sz && this.heap[rc][0] < this.heap[lc][0]) {
        mc = rc;
      }
      if (this.heap[idx][0] <= this.heap[mc][0]) {
        break;
      }
      this.swap(idx, mc);
      idx = mc;
    }
    return item;
  }

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }

  isEmpty() {
    return this.sz === 0;
  }
}

const dijkstra = (st) => {
  const pq = new MinHeap();
  dist[st] = 0;
  heap.push([dist[st], st]);
  while (!pq.isEmpty()) {
    const [d, v] = pq.pop();
    if (dist[v] !== d) {
      continue;
    }
    for (const [nd, nv] of graph[v]) {
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
