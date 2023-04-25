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

// 위상정렬 + dp
const solve = () => {
  const q = new Queue();
  const indegree = Array(n + 1).fill(0);
  const adj = [...Array(n + 1)].map(() => []);
  const dp = Array(n + 1).fill(0);
  for (const [x, y] of order) {
    adj[x].push(y);
    indegree[y]++;
  }
  for (let i = 1; i <= n; i++) {
    if (indegree[i] === 0) {
      q.push(i);
      dp[i] = d[i];
    }
  }
  while (!q.empty()) {
    const cur = q.front();
    q.pop();
    if (cur === w) {
      ans += dp[w] + "\n";
      return;
    }
    for (const nxt of adj[cur]) {
      indegree[nxt]--;
      dp[nxt] = Math.max(dp[nxt], dp[cur] + d[nxt]);
      if (indegree[nxt] === 0) {
        q.push(nxt);
      }
    }
  }
};

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map((x) => +x));
let n, k;
let d;
let order;
let w;
let ans = "";
let type = 1;
let cnt;
for (let i = 1; i < input.length; i++) {
  if (type === 1) {
    [n, k] = input[i];
    type++;
  } else if (type === 2) {
    // 함부로 0-index로 바꾸기보다는 d를 전처리
    d = [-1, ...input[i]];
    type++;
    cnt = k;
    order = [];
  } else if (type === 3) {
    order.push(input[i]);
    cnt--;
    if (cnt === 0) {
      type++;
    }
  } else {
    w = input[i][0];
    solve();
    type = 1;
  }
}
console.log(ans);
