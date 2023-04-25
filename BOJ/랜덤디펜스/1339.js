// 백트래킹이 정해가 아님
// 이 풀이는 O(N!)이지만 O(N)의 그리디 풀이가 존재함
const solve = () => {
  let sum = 0;
  for (let i = 0; i < n; i++) {
    let tmp = 0;
    for (let j = 0; j < arr[i].length; j++) {
      tmp = tmp * 10 + num[map.get(arr[i][j])];
    }
    sum += tmp;
  }
  ans = Math.max(ans, sum);
};

const dfs = (k) => {
  if (k === cnt) {
    solve();
    return;
  }
  for (let i = 0; i <= 9; i++) {
    if (vis[i]) {
      continue;
    }
    vis[i] = true;
    num[k] = i;
    dfs(k + 1);
    vis[i] = false;
  }
};

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
const n = Number(input[0]);
const arr = input.slice(1);
const map = new Map();
let cnt = 0;
for (let i = 0; i < n; i++) {
  for (let j = 0; j < arr[i].length; j++) {
    if (!map.has(arr[i][j])) {
      map.set(arr[i][j], cnt++);
    }
  }
}
const vis = Array(10).fill(false);
const num = Array(cnt).fill(-1);
let ans = 0;
dfs(0);
console.log(ans);
