const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

const n = parseInt(input[0]);
const graph = Array(n);
for (let i = 0; i < n; i++) {
  graph[i] = [];
}

for (let i = 0; i < n; i++) {
  const line = input[i + 1].split(' ').map((x) => +x);
  for (let j = 0; j < n; j++) {
    if (line[j] === 1) {
      graph[i].push(j);
    }
  }
}

let answer = '';

for (let i = 0; i < n; i++) {
  const stack = [i];
  const visited = Array(n).fill(0);
  while (stack.length > 0) {
    const cur = stack.pop();
    for (const next of graph[cur]) {
      if (visited[next] === 1) {
        continue;
      }
      visited[next] = 1;
      stack.push(next);
    }
  }
  for (let j = 0; j < n; j++) {
    answer += visited[j] + ' ';
  }
  answer += '\n';
}

console.log(answer);
