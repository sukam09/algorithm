const solve = (x, cur) => {
  if (x === k + 1) {
    ans.push(cur);
    return;
  }
  for (let i = 0; i <= 9; i++) {
    if (vis[i]) {
      continue;
    }
    if (x !== 0) {
      if (arr[x - 1] === "<") {
        if (num[x - 1] > i) {
          continue;
        }
      } else {
        if (num[x - 1] < i) {
          continue;
        }
      }
    }
    vis[i] = true;
    num[x] = i;
    solve(x + 1, cur + i); // string + number = string
    vis[i] = false;
  }
};

const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const k = Number(input[0]);
const arr = input[1].split(" ");
const num = Array(k + 1).fill(-1);
const ans = [];
const vis = Array(10).fill(false);
solve(0, "");
console.log(ans[ans.length - 1]);
console.log(ans[0]);
