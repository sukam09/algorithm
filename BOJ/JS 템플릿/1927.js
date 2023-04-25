class PriorityQueue {
  constructor() {
    this.pq = [];
    this.sz = 0;
  }

  push(x) {
    this.pq[++this.sz] = x;
    let cur = this.sz;
    while (cur > 1) {
      let p = parseInt(cur / 2);
      if (this.pq[p] <= this.pq[cur]) break;
      this.swap(p, cur);
      cur = p;
    }
  }

  top() {
    return this.pq[1];
  }

  pop() {
    this.pq[1] = this.pq[this.sz--];
    let cur = 1;
    while (cur * 2 <= this.sz) {
      const lc = cur * 2;
      const rc = cur * 2 + 1;
      let mc = lc;
      if (rc <= this.sz && this.pq[rc] < this.pq[lc]) mc = rc;
      if (this.pq[cur] <= this.pq[mc]) break;
      this.swap(cur, mc);
      cur = mc;
    }
  }

  swap(a, b) {
    [this.pq[a], this.pq[b]] = [this.pq[b], this.pq[a]];
  }

  empty() {
    return this.sz === 0;
  }
}

const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const n = +input[0];
const pq = new PriorityQueue();
let ans = '';
for (let i = 1; i <= n; i++) {
  const x = +input[i];
  if (x === 0) {
    if (pq.empty()) {
      ans += '0\n';
    } else {
      ans += pq.top() + '\n';
      pq.pop();
    }
  } else {
    pq.push(x);
  }
}
console.log(ans);
