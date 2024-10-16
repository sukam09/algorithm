const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(x => x.split(' ').map(Number));
const n = input[0][0];
const [u, v] = input[1];
const p = Array(n + 1).fill(0);
for (let i = 3; i < input.length; i++) {
  const [x, y] = input[i];
  p[y] = x;
}
const pu = [u];
const pv = [v];
let uu = u;
let vv = v;
while (p[uu] != 0) {
  uu = p[uu];
  pu.push(uu);
}
while (p[vv] != 0) {
  vv = p[vv];
  pv.push(vv);
}

const find = () => {
  for (let i = 0; i < pu.length; i++) {
    for (let j = 0; j < pv.length; j++) {
      if (pu[i] === pv[j]) {
        ans = i + j;
        return;
      }
    }
  }
  return -1;
};

let ans;
let lca = find();
if (lca === -1) {
  ans = -1;
}
console.log(ans);
