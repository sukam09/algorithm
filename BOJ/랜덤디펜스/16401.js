const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const [m, n] = input[0].split(' ').map(Number);
const l = input[1].split(' ').map(Number);
let st = 1;
let en = Math.max(...l);

const solve = mid => {
  let cnt = 0;
  for (let i = 0; i < n; i++) {
    cnt += Math.floor(l[i] / mid);
  }
  return cnt >= m;
};

let ans = 0;
while (st < en) {
  let mid = Math.floor((st + en + 1) / 2);
  if (solve(mid)) {
    st = mid;
    ans = st;
  } else {
    en = mid - 1;
  }
}
console.log(ans);
