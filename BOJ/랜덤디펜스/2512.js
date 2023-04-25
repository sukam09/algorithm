const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number));
const a = input[1];
const m = input[2][0];
let mx = 0;
for (const x of a) {
  mx = Math.max(mx, x);
}
let sum = 0;
for (const x of a) {
  sum += x;
}
if (sum <= m) {
  console.log(mx);
  process.exit();
}
for (let i = mx; i >= 1; i--) {
  let val = 0;
  let remain = m;
  let chk = true;
  for (const x of a) {
    if (x >= i) {
      val += i;
      remain -= i;
    } else {
      val += x;
      remain -= x;
    }
    if (remain < 0) {
      chk = false;
      break;
    }
  }
  if (chk) {
    console.log(i);
    process.exit();
  }
}
