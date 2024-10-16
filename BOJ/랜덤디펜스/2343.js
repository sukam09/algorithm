const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m] = input[0].split(' ').map(x => +x);
const arr = input[1].split(' ').map(x => +x);

let st = Math.max(...arr);
let en = arr.reduce((acc, cur) => acc + cur, 0);

const solve = x => {
  // 블루레이 길이가 x일 때 개수가 M 이하인가?
  let cnt = 1;
  let sum = 0;
  for (const item of arr) {
    if (sum + item <= x) {
      sum += item;
    } else {
      cnt++;
      sum = item;
    }
  }

  return cnt <= m;
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
