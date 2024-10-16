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

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const people = input[1].split(' ').sort();
const graph = {};
const indegrees = {};
const children = {};

for (const person of people) {
  graph[person] = [];
  indegrees[person] = 0;
  children[person] = [];
}

for (let i = 3; i < input.length; i++) {
  const [a, b] = input[i].split(' ');
  graph[b].push(a);
  indegrees[a]++;
}

const roots = [];
const queue = new Queue();
for (const person of people) {
  if (indegrees[person] === 0) {
    roots.push(person);
    queue.push(person);
  }
}

while (!queue.isEmpty()) {
  const cur = queue.pop();
  for (const next of graph[cur]) {
    indegrees[next]--;
    if (indegrees[next] === 0) {
      children[cur].push(next);
      queue.push(next);
    }
  }
}

let answer = '';
answer += `${roots.length}\n`;
answer += `${roots.join(' ')}\n`;
for (const person of people) {
  answer += `${person} ${children[person].length} ${children[person].sort().join(' ')}\n`;
}
console.log(answer);
