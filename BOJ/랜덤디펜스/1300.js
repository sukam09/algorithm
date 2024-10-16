const input = require('fs')
  .readFileSync(0)
  .toString()
  .trim()
  .split('\n')
  .map(v => +v);
const [n, k] = input;

let st = 1;
let en = k;

const solve = x => {
  let cnt = 0;
  for (let i = 1; i <= n; i++) {
    cnt += Math.min(Math.floor(x / i), n);
  }
  return cnt >= k;
};

while (st < en) {
  let mid = Math.floor((st + en) / 2);
  if (solve(mid)) {
    en = mid;
  } else {
    st = mid + 1;
  }
}

console.log(en);
