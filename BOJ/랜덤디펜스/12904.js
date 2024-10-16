const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [s, t] = input;

const reverse = s => {
  let ns = '';
  for (let i = s.length - 1; i >= 0; i--) {
    ns += s[i];
  }
  return ns;
};

let x = t;
while (x.length > s.length) {
  if (x[x.length - 1] === 'A') {
    x = x.slice(0, x.length - 1);
  } else {
    x = x.slice(0, x.length - 1);
    x = reverse(x);
  }
}
console.log(+(x === s));
