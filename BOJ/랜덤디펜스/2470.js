const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input[0]);
const a = input[1].split(' ').map(Number);
a.sort((x, y) => x - y);
let st = 0;
let en = n - 1;
let mn = Infinity;
let ans1, ans2;
// 양쪽 끝에서 가운데를 향하는 투 포인터 알고리즘
while (st < en) {
  const sum = a[st] + a[en];
  if (sum === 0) {
    console.log(a[st], a[en]);
    process.exit();
  }
  if (Math.abs(sum) < mn) {
    mn = Math.abs(sum);
    ans1 = a[st];
    ans2 = a[en];
  }
  if (sum < 0) {
    st++;
  } else {
    en--;
  }
}
console.log(ans1, ans2);
