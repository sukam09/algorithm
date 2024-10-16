const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(line => line.split(' ').map(Number));

const arrA = input[1];
const arrB = input[2];
const setB = new Set(arrB);

let answer = 0;
const elements = [];
for (const a of arrA) {
  if (!setB.has(a)) {
    answer++;
    elements.push(a);
  }
}
elements.sort((a, b) => a - b);

console.log(answer);
console.log(elements.join(' '));
