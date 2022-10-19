class Queue {
  constructor() {
    this.dat = [];
    this.head = 0;
    this.tail = 0;
  }

  push(item) {
    this.dat[this.tail++] = item;
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

  isEmpty() {
    return this.head === this.tail;
  }
}

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number));

const [n, m] = input[0];
const adj = [];
for (let i = 1; i <= n; i++) {
  adj[i] = [];
}
for (let i = 1; i <= m; i++) {
  const [a, b] = input[i];
  adj[b].push(a);
}

const bfs = (node) => {
  const q = new Queue();
  const vis = Array(n + 1).fill(false);
  q.push(node);
  vis[node] = true;
  let cnt = 1;
  while (!q.isEmpty()) {
    const cur = q.front();
    q.pop();
    for (let i = 0; i < adj[cur].length; i++) {
      const nxt = adj[cur][i];
      if (vis[nxt]) {
        continue;
      }
      q.push(nxt);
      vis[nxt] = true;
      cnt++;
    }
  }
  return cnt;
};

const hacked = [];
let mx = 0;
for (let i = 1; i <= n; i++) {
  hacked[i] = bfs(i);
  mx = Math.max(mx, hacked[i]);
}

let ans = "";
for (let i = 1; i <= n; i++) {
  if (hacked[i] === mx) {
    ans += i + " ";
  }
}
console.log(ans);
