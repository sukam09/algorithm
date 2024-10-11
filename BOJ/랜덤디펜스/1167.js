const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const v = +input[0];
const adj = [...Array(v + 1)].map(() => []);

for (let i = 1; i <= v; i++) {
  const line = input[i].split(' ').map(v => +v);
  const st = +line[0];
  const m = line.length;
  for (let j = 1; j < m - 1; j += 2) {
    const en = line[j];
    const dist = line[j + 1];
    adj[st].push([en, dist]);
  }
}

const d = Array(v + 1).fill(-1);

const dfs = v => {
  for (const [nv, nd] of adj[v]) {
    if (d[nv] !== -1) {
      continue;
    }
    d[nv] = d[v] + nd;
    dfs(nv);
  }
};

d[1] = 0;
dfs(1);
const mx = Math.max(...d);
let tg = 0;
for (let i = 1; i <= v; i++) {
  if (d[i] === mx) {
    tg = i;
    break;
  }
}

for (let i = 0; i < d.length; i++) {
  d[i] = -1;
}

d[tg] = 0;
dfs(tg);
console.log(Math.max(...d));
