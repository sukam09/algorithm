const input = require('fs').readFileSync('/dev/stdin').toString().trim();
let ans = '';
const stk = [];

for (let i = 0; i < input.length; i++) {
  const c = input[i];
  if (c >= 'A' && c <= 'Z') {
    ans += c;
  } else if (c === '(') {
    stk.push(c);
  } else if (c === '*' || c === '/') {
    while (stk.length > 0 && (stk[stk.length - 1] === '*' || stk[stk.length - 1] === '/')) {
      ans += stk.pop();
    }
    stk.push(c);
  } else if (c === '+' || c === '-') {
    while (stk.length > 0 && stk[stk.length - 1] !== '(') {
      ans += stk.pop();
    }
    stk.push(c);
  } else {
    // )
    while (stk.length > 0 && stk[stk.length - 1] !== '(') {
      ans += stk.pop();
    }
    stk.pop();
  }
}

while (stk.length > 0) {
  ans += stk.pop();
}

console.log(ans);