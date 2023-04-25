const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number));

// 에라토스테네스의 체
const p = Array(1000001).fill(true);
p[0] = false;
p[1] = false;
for (let i = 2; i * i <= 1000000; i++) {
  if (!p[i]) {
    continue;
  }
  for (let j = i * i; j <= 1000000; j += i) {
    p[j] = false;
  }
}
let ans = "";
for (let i = 0; i < input.length - 1; i++) {
  const x = input[i][0]; // input[i]가 숫자가 아닌 배열임에 주의
  let found = false;
  for (let i = 1; i <= x / 2; i += 2) {
    const j = x - i;
    if (j % 2 === 1 && p[i] && p[j]) {
      ans += `${x} = ${i} + ${j}\n`;
      found = true;
      break;
    }
  }
  if (!found) {
    ans += "Goldbach's conjecture is wrong.\n";
  }
}
console.log(ans);
