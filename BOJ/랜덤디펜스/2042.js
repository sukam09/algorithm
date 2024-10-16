const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m, k] = input[0].split(' ').map(v => +v);

const arr = Array(n + 1).fill(BigInt(0));
const BIT = Array(n + 1).fill(BigInt(0));
let ans = '';

const add = (idx, val) => {
  while (idx <= n) {
    BIT[idx] += BigInt(val);
    idx += idx & -idx;
  }
};

const sum = idx => {
  let s = BigInt(0);
  while (idx > 0) {
    s += BIT[idx];
    idx -= idx & -idx;
  }
  return s;
};

for (let i = 1; i <= n; i++) {
  arr[i] = BigInt(input[i]);
  add(i, arr[i]);
}

for (let i = n + 1; i < input.length; i++) {
  const [a, b, c] = input[i].split(' ').map(v => +v);

  if (a === 1) {
    add(b, BigInt(c) - arr[b]);
    arr[b] = BigInt(c);
  } else {
    ans += sum(c) - sum(b - 1) + '\n';
  }
}
console.log(ans);
/*
BIT(Binary Indexed Tree) or 펜윅 트리 풀이
BIT 배열의 크기는 N + 1로 두면 됨
세그먼트 트리로도 풀 수 있음 단, 이 경우 배열의 크기를 4N으로 두어야 함
입력 범위가 Number 범위를 넘어가므로 BigInt를 사용하지 않으면 오답
*/
