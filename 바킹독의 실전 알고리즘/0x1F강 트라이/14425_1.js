class Node {
  constructor(c) {
    this.word = c;
    this.fin = 0;
    this.map = {};
  }
}

const input = require('fs').readFileSync(0).toString().trim().split('\n');
let [n, m] = input[0].split(' ').map(v => +v);
let idx = 1;
let ans = 0;
const root = new Node('');

const insert = s => {
  let cur = root;
  for (const c of s) {
    if (!cur.map[c]) {
      const node = new Node(c);
      cur.map[c] = node;
    }
    cur = cur.map[c];
  }
  cur.fin = 1;
};

const find = s => {
  let cur = root;
  for (const c of s) {
    if (!cur.map[c]) {
      return 0;
    }
    cur = cur.map[c];
  }
  return cur.fin === 1;
};

while (n--) {
  const s = input[idx++];
  insert(s);
}

while (m--) {
  const s = input[idx++];
  ans += find(s);
}

console.log(ans);