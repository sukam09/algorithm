const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const map = new Map();
const alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const p = input[1];

for (let i = 2; i < input.length; i++) {
  const idx = i - 2;
  map.set(alpha[idx], Number(input[i]));
}

const stk = [];

const calc = (a, b, op) => {
  if (op == '+') {
    return a + b;
  } else if (op == '-') {
    return a - b;
  } else if (op == '*') {
    return a * b;
  } else {
    return a / b;
  }
}

for (const x of p) {
  if (alpha.includes(x)) {
    stk.push(map.get(x));
  } else {
    const op = x;
    const b = stk.pop();
    const a = stk.pop();
    const res = calc(a, b, op);
    stk.push(res);
  }
}

console.log(stk[0].toFixed(2));