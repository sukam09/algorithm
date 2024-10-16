class PriorityQueue {
  constructor() {
    this.heap = [];
    this.sz = 0;
  }

  push(x) {
    this.heap[++this.sz] = x;
    let cur = this.sz;
    while (cur > 1) {
      let p = parseInt(cur / 2);
      if (this.heap[p] >= this.heap[cur]) break;
      this.swap(p, cur);
      cur = p;
    }
  }

  top() {
    return this.heap[1];
  }

  pop() {
    this.heap[1] = this.heap[this.sz--];
    let cur = 1;
    while (cur * 2 <= this.sz) {
      const lc = cur * 2;
      const rc = cur * 2 + 1;
      let mc = lc;
      if (rc <= this.sz && this.heap[rc] > this.heap[lc]) mc = rc;
      if (this.heap[cur] >= this.heap[mc]) break;
      this.swap(cur, mc);
      cur = mc;
    }
  }

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }

  empty() {
    return this.sz === 0;
  }
}

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, k] = input[0].split(' ').map(v => +v);
const m = Array(n).fill(0);
const v = Array(n).fill(0);
const c = Array(k).fill(0);
const mv = [];

let idx = 1;
for (let i = 0; i < n; i++) {
  const [mm, vv] = input[idx++].split(' ').map(v => +v);
  m[i] = mm;
  v[i] = vv;
  mv.push([mm, vv]);
}
for (let i = 0; i < k; i++) {
  const cc = +input[idx++];
  c[i] = cc;
}

const pq = new PriorityQueue();
mv.sort((a, b) => a[0] - b[0]);
c.sort((a, b) => a - b);

let j = 0;
let ans = 0;
for (let i = 0; i < k; i++) {
  while (j < n && mv[j][0] <= c[i]) {
    pq.push(mv[j++][1]);
  }

  if (!pq.empty()) {
    ans += pq.top();
    pq.pop();
  }
}

console.log(ans);
