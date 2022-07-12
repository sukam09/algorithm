const [n, m, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(/\s/)
  .map(Number);

const graph = Array(n + 1);
for (let i = 0; i < n + 1; i++) {
  graph[i] = [];
}

for (let i = 0; i < input.length; i += 2) {
  const [a, b] = [input[i], input[i + 1]];
  graph[a].push(b);
  graph[b].push(a);
}

const fff = new Set();
for (const f of graph[1]) {
  fff.add(f);
  for (const ff of graph[f]) {
    fff.add(ff);
  }
}

fff.delete(1);
console.log(fff.size);
