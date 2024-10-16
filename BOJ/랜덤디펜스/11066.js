// 재귀 top-down dp
// 다른 방식도 나중에 공부해볼것
const dp = (st, en) => {
  if (d[st][en] !== Infinity) {
    return d[st][en];
  }
  if (st === en) {
    return (d[st][en] = 0);
  }
  if (st + 1 === en) {
    return (d[st][en] = cost[st] + cost[en]);
  }
  for (let mid = st; mid < en; mid++) {
    d[st][en] = Math.min(d[st][en], dp(st, mid) + dp(mid + 1, en) + s[en] - s[st - 1]);
  }
  return d[st][en];
};

const solve = () => {
  cost = [0, ...arr];
  d = [...Array(k + 1)].map(() => Array(k + 1).fill(Infinity));
  s = Array(k + 1).fill(0);
  for (let i = 1; i <= k; i++) {
    s[i] = s[i - 1] + cost[i];
  }
  ans += dp(1, k) + '\n';
};

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let k, arr, d, cost, s;
let ans = '';
for (let i = 1; i < input.length; i += 2) {
  k = Number(input[i]);
  arr = input[i + 1].split(' ').map(Number);
  solve();
}
console.log(ans);
