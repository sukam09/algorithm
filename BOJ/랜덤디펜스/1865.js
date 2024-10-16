const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let n, m, w;
let ccnt = 0;
let tcnt = 0;
let ans = '';
let adj;
const INF = 1e9;

const solve = () => {
  const dist = Array(n + 1).fill(INF);
  dist[1] = 0;
  for (let i = 0; i < n; i++) {
    for (const [t, s, e] of adj) {
      if (dist[s] + t < dist[e]) {
        dist[e] = dist[s] + t;
        if (i === n - 1) {
          ans += 'YES\n';
          return;
        }
      }
    }
  }
  ans += 'NO\n';
};

for (let i = 1; i < input.length; i++) {
  if (ccnt === tcnt) {
    if (i > 1) {
      solve();
    }

    // initialization
    [n, m, w] = input[i].split(' ').map(v => +v);
    adj = [];
    ccnt = 0;
    tcnt = m + w;
  } else {
    const [s, e, t] = input[i].split(' ').map(v => +v);
    if (ccnt < m) {
      adj.push([t, s, e]);
      adj.push([t, e, s]);
    } else {
      adj.push([-t, s, e]);
    }
    ccnt++;
  }
}

solve();
console.log(ans);
