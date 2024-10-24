const input = require('fs').readFileSync(0).toString().trim().split('\n');
const s1 = '`1234567890-=';
const s2 = 'qwertyuiop[]\\';
const s3 = "asdfghjkl;'";
const s4 = 'zxcvbnm,./';
const keyboard = [s1, s2, s3, s4];
const map = new Map();
for (let i = 0; i < keyboard.length; i++) {
  for (const c of keyboard[i]) {
    map.set(c, i);
  }
}

let ans = '';
const solve = s => {
  let ret = '';
  for (const c of s) {
    if (c === ' ') ret += c;
    else {
      const i = map.get(c);
      const j = keyboard[i].indexOf(c);
      ret += keyboard[i][j - 1];
    }
  }
  ans += ret.toUpperCase() + '\n';
};

for (const s of input) {
  solve(s.toLowerCase());
}

console.log(ans);