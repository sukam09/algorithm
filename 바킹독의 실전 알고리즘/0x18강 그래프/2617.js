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

const bfs = (start, nodes) => {
  const queue = new Queue();
  const visited = Array(n + 1).fill(false);
  queue.push(start);
  visited[start] = true;
  let nodeNum = 0;

  while (!queue.isEmpty()) {
    const cur = queue.pop();
    for (const next of nodes[cur]) {
      if (visited[next]) {
        continue;
      }
      visited[next] = true;
      nodeNum++;
      queue.push(next);
    }
  }
  return nodeNum;
};

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m] = input[0].split(' ').map(Number);
const parentNodes = [];
const childNodes = [];
for (let i = 1; i <= n; i++) {
  parentNodes[i] = [];
  childNodes[i] = [];
}

for (let i = 1; i <= m; i++) {
  const [parent, child] = input[i].split(' ').map(Number);
  parentNodes[child].push(parent);
  childNodes[parent].push(child);
}

const target = (n + 1) / 2;
let answer = 0;

for (let i = 1; i <= n; i++) {
  const [parentNum, childNum] = [bfs(i, parentNodes), bfs(i, childNodes)];
  if (parentNum >= target || childNum >= target) {
    answer++;
  }
}

console.log(answer);
