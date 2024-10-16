const dist = (x1, y1, x2, y2) => (x2 - x1) ** 2 + (y2 - y1) ** 2;

const solve = () => {
  const chk = Array(circle.length).fill(false);
  for (let i = 0; i < circle.length; i++) {
    const [x, y, r] = circle[i];
    if (dist(x1, y1, x, y) < r ** 2) {
      chk[i] = !chk[i];
    }
    if (dist(x2, y2, x, y) < r ** 2) {
      chk[i] = !chk[i];
    }
  }
  ans += chk.filter(x => x).length + '\n';
};

const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(x => x.split(' ').map(Number));
let circle = [];
let x1, y1, x2, y2;
let cnt;
let ans = '';
for (let i = 1; i < input.length; i++) {
  if (input[i].length === 4) {
    [x1, y1, x2, y2] = input[i];
    cnt = -1;
  } else if (input[i].length === 1) {
    cnt = input[i][0];
    circle = [];
  } else {
    circle.push(input[i]);
    cnt--;
  }
  if (cnt === 0) {
    solve();
  }
}
console.log(ans);
