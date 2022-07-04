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

const bfs = (cur, graph, colors) => {
  const queue = new Queue();
  queue.push(cur);
  colors[cur] = 1;

  while (!queue.isEmpty()) {
    const node = queue.pop();
    const color = colors[node];
    for (const next of graph[node]) {
      if (colors[next] !== 0) {
        continue;
      }
      colors[next] = 3 - color;
      queue.push(next);
    }
  }
};

const isBipartite = (v, graph) => {
  const colors = Array(v + 1).fill(0);
  for (let i = 1; i <= v; i++) {
    if (colors[i] === 0) {
      bfs(i, graph, colors);
    }
  }

  for (let i = 1; i <= v; i++) {
    for (const next of graph[i]) {
      if (colors[i] === colors[next]) {
        return false;
      }
    }
  }
  return true;
};

const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

let k = Number(input[0]);
let i = 1;
let answer = '';

while (k--) {
  let [v, e] = input[i].split(' ').map(Number);
  graph = Array(v + 1);
  for (let j = 1; j <= v; j++) {
    graph[j] = [];
  }
  i++;
  while (e--) {
    const [a, b] = input[i].split(' ').map(Number);
    graph[a].push(b);
    graph[b].push(a);
    i++;
  }
  answer += isBipartite(v, graph) ? 'YES\n' : 'NO\n';
}

console.log(answer);
