const input = require('fs').readFileSync(0).toString().trim().split('\n');
const [n, m, l] = input[0].split(' ').map(v => +v);
const arr = n > 0 ? [0, ...input[1].split(' ').map(v => +v), l] : [0, l];
arr.sort((a, b) => a - b);

const diff = [];
for (let i = 1; i < arr.length; i++) {
  diff.push(arr[i] - arr[i - 1]);
}

let st = 1;
let en = Math.max(...diff);

const solve = x => {
  let cnt = 0;
  for (let i = 0; i < diff.length; i++) {
    if (diff[i] > x) {
      let q = Math.floor(diff[i] / x);
      const r = diff[i] % x;
      if (r === 0) {
        q--;
      }
      cnt += q;
    }
    if (cnt > m) {
      return 0;
    }
  }
  return 1;
};

while (st < en) {
  const mid = Math.floor((st + en) / 2);
  if (solve(mid)) {
    en = mid;
  } else {
    st = mid + 1;
  }
}

console.log(en);
