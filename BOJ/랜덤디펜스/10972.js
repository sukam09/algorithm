const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input[0]);
const arr = input[1].split(' ').map(Number);

// 때로는 풀이가 잘 떠올르지 않는다면 직접 그려서 직관적으로 한번 생각해보자
// next_permutation
let idx = -1;
for (let i = n - 2; i >= 0; i--) {
  if (arr[i] < arr[i + 1]) {
    idx = i;
    break;
  }
}
if (idx === -1) {
  console.log(-1);
  process.exit();
}
let mn = n + 1;
let target;
for (let i = idx + 1; i < n; i++) {
  if (arr[i] > arr[idx] && arr[i] < mn) {
    mn = arr[i];
    target = i;
  }
}
[arr[idx], arr[target]] = [arr[target], arr[idx]];
const ans = [...arr.slice(0, idx + 1), ...arr.slice(idx + 1).sort((a, b) => a - b)];
console.log(ans.join(' '));
