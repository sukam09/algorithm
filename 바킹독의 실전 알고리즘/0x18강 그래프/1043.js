class Queue {
  constructor() {
    this.queue = [];
    this.head = 0;
    this.tail = 0;
  }

  push(item) {
    this.queue[this.tail++] = item;
  }

  pop() {
    return this.queue[this.head++];
  }

  isEmpty() {
    return this.tail - this.head === 0;
  }
}

const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');
const [n, m] = input[0].split(' ').map(Number);

const graph = [];
for (let i = 1; i <= n; i++) {
  graph[i] = [];
}

let start;

for (let i = 1; i < input.length; i++) {
  const [p, ...pp] = input[i].split(' ').map(Number);
  if (p === 0) {
    console.log(m);
    process.exit();
  }
  if (i === 1) {
    start = pp[0];
  }
  if (p === 1) {
    continue;
  }
  for (let j = 0; j < p - 1; j++) {
    const [a, b] = [pp[j], pp[j + 1]];
    graph[a].push(b);
    graph[b].push(a);
  }
}

const queue = new Queue();
const visited = Array(n + 1).fill(false);
queue.push(start);
visited[start] = true;
while (!queue.isEmpty()) {
  const cur = queue.pop();
  for (const next of graph[cur]) {
    if (visited[next]) {
      continue;
    }
    visited[next] = true;
    queue.push(next);
  }
}

let answer = 0;
for (let i = 2; i < input.length; i++) {
  const line = input[i].split(' ').map(Number);
  let inflated = true;
  for (let j = 1; j < line.length; j++) {
    if (visited[line[j]]) {
      inflated = false;
      break;
    }
  }
  if (inflated) {
    answer++;
  }
}

console.log(answer);
