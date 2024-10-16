const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = input[0].split(' ').map(Number)[0];
const max = n * 500 + 5;
const next = Array(max);
for (let i = 0; i < max; i++) {
  next[i] = Array(26).fill(-1);
}
const check = Array(max).fill(false);
const root = 1;
let unused = 2;

const charToInt = char => char.charCodeAt(0) - 'a'.charCodeAt(0);

const insert = string => {
  let cur = root;
  for (const char of string) {
    if (next[cur][charToInt(char)] === -1) {
      next[cur][charToInt(char)] = unused++;
    }
    cur = next[cur][charToInt(char)];
  }
  check[cur] = true;
};

const find = string => {
  let cur = root;
  for (const char of string) {
    if (next[cur][charToInt(char)] === -1) {
      return false;
    }
    cur = next[cur][charToInt(char)];
  }
  return check[cur];
};

let answer = 0;
for (let i = 1; i < input.length; i++) {
  const string = input[i];
  if (i <= n) {
    insert(string);
  } else {
    if (find(string)) {
      answer++;
    }
  }
}
console.log(answer);
