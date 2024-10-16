const dfs = idx => {
  if (idx === cnt) {
    input.forEach(x => (ans += `${x.join(' ')}\n`));
    console.log(ans);
    process.exit();
  }
  const [x, y] = cand[idx];
  for (let i = 1; i <= 9; i++) {
    const section = 3 * parseInt(x / 3) + parseInt(y / 3);
    if (a1[x][i] || a2[y][i] || a3[section][i]) {
      continue;
    }
    a1[x][i] = true;
    a2[y][i] = true;
    a3[section][i] = true;
    input[x][y] = i;
    dfs(idx + 1);
    a1[x][i] = false;
    a2[y][i] = false;
    a3[section][i] = false;
    input[x][y] = 0;
  }
};

const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(x => x.split(' ').map(Number));
const a1 = Array(9)
  .fill()
  .map(() => Array(10).fill(false));
const a2 = Array(9)
  .fill()
  .map(() => Array(10).fill(false));
const a3 = Array(9)
  .fill()
  .map(() => Array(10).fill(false));
let cnt = 0;
const cand = [];
for (let i = 0; i < 9; i++) {
  for (let j = 0; j < 9; j++) {
    if (input[i][j] === 0) {
      cnt++;
      cand.push([i, j]);
      continue;
    }
    const cur = input[i][j];
    a1[i][cur] = true;
    a2[j][cur] = true;
    const section = 3 * parseInt(i / 3) + parseInt(j / 3);
    a3[section][cur] = true;
  }
}
let ans = '';
dfs(0);
