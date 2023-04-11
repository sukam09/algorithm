const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n').map(Number);
const postorder = (s, e) => {
  if (s > e) return;
  let mid = e + 1;
  for (let i = s + 1; i <= e; i++) {
    if (input[i] > input[s]) {
      mid = i;
      break;
    }
  }
  postorder(s + 1, mid - 1);
  postorder(mid, e);
  ans += input[s] + '\n';
};

let ans = '';
postorder(0, input.length - 1);
console.log(ans);
