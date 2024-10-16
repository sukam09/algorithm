// 맞은 순대로는 아니고 우연히 발견한 문제
// 정렬 + 그리디
// 난이도는 쉽지만 생각보다 발상을 떠올리는데 오래걸림
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, l] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);
arr.sort((a, b) => a - b);
let ans = 0;
let en = 0;
for (let i = 0; i < n; i++) {
  const k = arr[i];
  if (en < k - 0.5) {
    ans++;
    en = k - 0.5 + l;
  } else if (en < k + 0.5) {
    ans++;
    en += l;
  }
}
console.log(ans);
