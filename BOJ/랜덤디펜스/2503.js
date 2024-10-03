const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = +input[0];
const arr = input.slice(1).map(v => v.split(' ').map(v => +v));

const chk = num => {
  const s = num.toString();
  if (s.includes('0')) {
    return 0;
  }

  if (s[0] === s[1] || s[1] === s[2] || s[2] === s[0]) {
    return 0;
  }

  return 1;
}

const cands = [];
const sbx = 'SBX';
const res = Array(3).fill('');

const dfs = k => {
  if (k === 3) {
    cands.push(res.join(''));
    return;
  }
  for (let i = 0; i < 3; i++) {
    res[k] = sbx[i];
    dfs(k + 1);
  }
};
dfs(0);

const solve = (num, s, b, target) => {
  const orders = [];
  for (const cand of cands) {
    let ss = 0;
    let bb = 0;
    for (const c of cand) {
      if (c === 'S') {
        ss++;
      } else if (c === 'B') {
        bb++;
      }
    }
    if (ss === s && bb === b) {
      orders.push(cand);
    }
  }

  ns = num.toString();
  ts = target.toString();

  for (const order of orders) {
    let ac = 0;
    for (let i = 0; i < 3; i++) {
      if (order[i] === 'S') {
        // strike
        if (ns[i] === ts[i]) {
          ac++;
        }
      } else if (order[i] === 'B') {
        // ball
        if (ts.includes(ns[i]) && ts.indexOf(ns[i]) !== i) {
          ac++;
        }
      } else {
        // not strike nor ball
        if (ns[i] !== ts[i] && !(ts.includes(ns[i]) && ts.indexOf(ns[i]) !== i)) {
          ac++;
        }
      }
    }

    if (ac === 3) {
      return 1;
    }
  }

  return 0;
};

let ans = 0;
for (let i = 111; i <= 999; i++) {
  if (!chk(i)) {
    continue;
  }

  let cnt = 0;
  for (const [num, s, b] of arr) {
    if (solve(num, s, b, i)) {
      cnt++;
    }
  }
  if (cnt === n) {
    ans++;
  }
}

console.log(ans);