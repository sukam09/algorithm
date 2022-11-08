const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
const n = Number(input[0]);
const dist = [...Array(n)].map(() => Array(n).fill(Infinity));
for (let i = 2; i < n + 2; i++) {
  const r = i - 2;
  const line = input[i].split(" ").map(Number);
  for (let j = 0; j < n; j++) {
    dist[r][j] = line[j] === 0 ? Infinity : 1;
  }
}
for (let i = 0; i < n; i++) {
  dist[i][i] = 0;
}
for (let k = 0; k < n; k++) {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
    }
  }
}
const route = input[input.length - 1].split(" ").map(Number);
for (let i = 0; i < route.length - 1; i++) {
  const [u, v] = [route[i], route[i + 1]];
  if (dist[u - 1][v - 1] === Infinity) {
    console.log("NO");
    process.exit();
  }
}
console.log("YES");
