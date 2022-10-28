const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
let [n, m, b] = input[0].split(" ").map(Number);
const board = input.slice(1).map((x) => x.split(" ").map(Number));
let ans1 = Infinity;
let ans2 = -1;
for (let h = 0; h <= 256; h++) {
  let removed = 0;
  let made = 0;
  let time = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j] > h) {
        removed += board[i][j] - h;
        time += 2 * (board[i][j] - h);
      } else if (board[i][j] < h) {
        made += h - board[i][j];
        time += h - board[i][j];
      }
    }
  }
  if (b + removed - made >= 0) {
    if (time <= ans1) {
      ans1 = time;
      ans2 = Math.max(ans2, h);
    }
  }
}
console.log(ans1, ans2);
