const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = +input[0];
const arr = input[1].split(' ').map(v => +v);
arr.sort((a, b) => a - b);

let st, en;
let mn = 4000000000;
let ans; // ans에 후보군 하나만 담는게 아니고 모두 담을 경우 메모리 초과 발생
for (let i = 0; i < n - 2; i++) {
  let sum = 0;
  st = i + 1; // st의 초기값을 i + 1로 두어 정렬할 필요가 없게끔 하는 테크닉을 잘 알아두자
  en = n - 1;
  while (st < en) {
    sum = arr[i] + arr[st] + arr[en];
    const cand = [arr[i], arr[st], arr[en]]; // 여기서 정렬할 경우 시간 초과 발생
    const abs = Math.abs(sum);
    if (abs < mn) {
      mn = abs;
      ans = cand;
    }
    if (sum <= 0) {
      st++;
    } else {
      en--;
    }
  }
}

console.log(...ans);
/*
시간 제한과 메모리 제한이 빡빡한 문제
*/
