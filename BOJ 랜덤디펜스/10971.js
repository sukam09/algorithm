const dfs = (idx, hist) => {
  if (idx === n) {
    // 시작 지점으로 돌아오는 경로가 있는지 확인해줘야함
    if (w[hist[hist.length - 1]][hist[0]] === 0) {
      return;
    }
    hist.push(hist[0]);
    let sum = 0;
    for (let i = 0; i < hist.length - 1; i++) {
      sum += w[hist[i]][hist[i + 1]];
    }
    ans = Math.min(ans, sum);
    return;
  }
  for (let i = 0; i < n; i++) {
    if (vis[i] || (hist.length > 0 && w[hist[hist.length - 1]][i] === 0)) {
      continue;
    }
    vis[i] = true;
    dfs(idx + 1, [...hist, i]);
    vis[i] = false;
  }
};

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map((x) => +x));
const n = input[0][0];
const w = input.slice(1);
let ans = Infinity;
const vis = Array(n).fill(false);
dfs(0, []);
console.log(ans);
