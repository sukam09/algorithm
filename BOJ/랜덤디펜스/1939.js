const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const [n, m] = input[0].split(' ').map(Number);
const adj = Array(n + 1)
  .fill()
  .map(() => []);
for (let i = 1; i <= m; i++) {
  const [a, b, c] = input[i].split(' ').map(Number);
  adj[a].push([b, c]);
  adj[b].push([a, c]);
}
const [u, v] = input[input.length - 1].split(' ').map(Number);

class Queue {
  constructor() {
    this.front = 0;
    this.rear = 0;
    this.q = [];
  }

  push(x) {
    this.q[this.rear++] = x;
  }

  top() {
    return this.q[this.front];
  }

  pop() {
    this.front++;
  }

  empty() {
    return this.front === this.rear;
  }
}

const solve = x => {
  const vis = Array(n + 1).fill(0);
  vis[u] = 1;
  const q = new Queue();
  q.push(u);
  while (!q.empty()) {
    const cur = q.top();
    q.pop();
    if (cur === v) return 1;
    for (const [nxt, w] of adj[cur]) {
      if (vis[nxt]) continue;
      if (x > w) continue;
      vis[nxt] = 1;
      q.push(nxt);
    }
  }
  return 0;
};

let st = 1;
let en = 1000000000;
while (st < en) {
  const mid = parseInt((st + en + 1) / 2);
  if (solve(mid)) {
    st = mid;
  } else {
    en = mid - 1;
  }
}
console.log(st);
