class Queue {
  constructor() {
    this.queue = Array(55);
    this.head = 0;
    this.tail = 0;
  }

  push(x) {
    this.queue[this.tail++] = x;
  }

  pop() {
    return this.queue[this.head++];
  }

  isEmpty() {
    return this.tail - this.head === 0;
  }
}

const [n, ...input] = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split(/\s/)
  .map(Number);

const graph = Array(n + 1);
for (let i = 1; i <= n; i++) {
  graph[i] = [];
}

for (let i = 0; i < input.length - 2; i += 2) {
  const [a, b] = [input[i], input[i + 1]];
  graph[a].push(b);
  graph[b].push(a);
}

const scores = Array(n + 1).fill(50);

for (let i = 1; i <= n; i++) {
  const dists = Array(n + 1).fill(-1);
  const queue = new Queue();
  queue.push([0, i]);
  dists[i] = 0;
  while (!queue.isEmpty()) {
    const [dist, cur] = queue.pop();
    for (const next of graph[cur]) {
      if (dists[next] !== -1) {
        continue;
      }
      dists[next] = dist + 1;
      queue.push([dists[next], next]);
    }
  }
  scores[i] = Math.max(...dists);
}

const presidentScore = Math.min(...scores);
let presidentNum = 0;
let presidentCandidate = '';

for (let i = 1; i <= n; i++) {
  if (scores[i] === presidentScore) {
    presidentNum++;
    presidentCandidate += `${i} `;
  }
}

const answer = `${presidentScore} ${presidentNum}\n${presidentCandidate.trim()}`;
console.log(answer);
