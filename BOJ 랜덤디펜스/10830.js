const matmul = (a, b) => {
  const ret = [...Array(n)].map(() => Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      for (let k = 0; k < n; k++) {
        ret[i][j] += (a[i][k] * b[k][j]) % 1000;
      }
      ret[i][j] %= 1000;
    }
  }
  return ret;
};

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
const n = input[0].split(" ").map(Number)[0];
let a = input.slice(1).map((x) => x.split(" ").map(Number));
let b = input[0].split(" ").map(Number)[1];
let ans = [...Array(n)].map(() => Array(n).fill(0));
for (let i = 0; i < n; i++) {
  ans[i][i] = 1; // 단위행렬
}
// 분할 정복을 이용한 거듭제곱
while (b > 0) {
  if (b % 2 === 1) {
    ret = matmul(ret, a);
    b--;
  } else {
    a = matmul(a, a);
    b /= 2;
  }
}
let output = "";
ans.forEach((x) => (output += x.join(" ") + "\n"));
console.log(output);
