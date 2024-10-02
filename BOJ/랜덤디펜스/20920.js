const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m] = input[0].split(' ').map(x => +x);
const arr = input.slice(1);

const set = new Set();
const counter = new Map();

for (const x of arr) {
  if (x.length >= m) {
    set.add(x);
    if (counter.has(x)) {
      counter.set(x, counter.get(x) + 1);
    } else {
      counter.set(x, 1);
    }
  }
}

const arr2 = Array.from(set);

arr2.sort((a, b) => {
  if (counter.get(a) > counter.get(b)) {
    return -1;
  } else if (counter.get(a) < counter.get(b)) {
    return 1;
  } else {
    if (a.length > b.length) {
      return -1;
    } else if (a.length < b.length) {
      return 1;
    } else {
      if (a < b) {
        return -1;
      } else if (a > b) {
        return 1;
      } else {
        return 0;
      }
    }
  }
})

console.log(arr2.join('\n'));