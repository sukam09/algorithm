const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(x => x.split(' ').map(Number));
const x = input[0][0];
const a = [64];
while (true) {
  let sum = 0;
  for (const aa of a) {
    sum += aa;
  }
  if (sum <= x) {
    break;
  }
  const en = a.pop();
  a.push(en / 2);
  a.push(en / 2);
  sum = 0;
  for (let i = 0; i < a.length - 1; i++) {
    sum += a[i];
  }
  if (sum >= x) {
    a.pop();
  }
}
console.log(a.length);
