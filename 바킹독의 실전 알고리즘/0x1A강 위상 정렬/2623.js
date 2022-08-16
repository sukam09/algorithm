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

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map((x) => +x));

const n = input[0][0];
const indegrees = Array(n + 1).fill(0);
const graph = Array(n + 1);
for (let i = 1; i <= n; i++) {
  graph[i] = [];
}

for (let i = 1; i < input.length; i++) {
  for (let j = 1; j < input[i].length - 1; j++) {
    const [a, b] = [input[i][j], input[i][j + 1]];
    graph[a].push(b);
    indegrees[b]++;
  }
}

const queue = new Queue();
for (let i = 1; i <= n; i++) {
  if (indegrees[i] === 0) {
    queue.push(i);
  }
}

let answer = "";
let count = 0;
while (!queue.isEmpty()) {
  const cur = queue.pop();
  answer += `${cur}\n`;
  count++;
  for (const next of graph[cur]) {
    indegrees[next]--;
    if (indegrees[next] === 0) {
      queue.push(next);
    }
  }
}

console.log(count === n ? answer : 0);
