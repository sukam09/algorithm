class Queue {
  constructor() {
    this.data = [];
    this.head = 0;
    this.tail = 0;
  }

  push(item) {
    this.data[this.tail++] = item;
  }

  pop() {
    this.head++;
  }

  front() {
    return this.data[this.head];
  }

  rear() {
    return this.data[this.tail - 1];
  }

  isEmpty() {
    return this.head === this.tail;
  }
}

const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(line => line.split(' ').map(Number));

const [n, m] = input[0];
const graph = [];
for (let i = 1; i <= n; i++) {
  graph[i] = [];
}
for (let i = 1; i <= m; i++) {
  const [a, b] = input[i];
  graph[a].push(b);
  graph[b].push(a);
}

const queue = new Queue();
const dists = Array(n + 1).fill(-1);
queue.push(1);
dists[1] = 0;
while (!queue.isEmpty()) {
  const cur = queue.front();
  queue.pop();
  for (const next of graph[cur]) {
    if (dists[next] !== -1) {
      continue;
    }
    queue.push(next);
    dists[next] = dists[cur] + 1;
  }
}

const maxval = Math.max(...dists);
const index = dists.indexOf(maxval);
const count = dists.filter(dist => dist === maxval).length;
console.log(index, maxval, count);
