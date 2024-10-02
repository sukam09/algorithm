const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = +input[0];
const arr = input[1].split(' ').map(x => +x);

class Queue {
  constructor() {
    this.front = 0;
    this.rear = 0;
    this.dat = [];
  }

  push(x) {
    this.dat[this.rear++] = x;
  }

  top() {
    return this.dat[this.front];
  }

  pop() {
    this.front++;
  }

  empty() {
    return this.front === this.rear;
  }

  size() {
    return this.rear - this.front;
  }
}

const q = new Queue();
let nxt = 1;
for (const x of arr) {
  q.push(x);
}

const stk = [];
while (!q.empty()) {
  if (q.top() === nxt) {
    q.pop();
    nxt++;
  } else {
    if (stk.length > 0) {
      if (stk[stk.length - 1] === nxt) {
        stk.pop();
        nxt++;
      } else {
        stk.push(q.top());
        q.pop();
      }
    } else {
      stk.push(q.top());
      q.pop();
    }
  }
}

while (stk.length > 0) {
  const top = stk[stk.length - 1];
  if (top !== nxt) {
    console.log('Sad');
    process.exit(0);
  } else {
    stk.pop();
    nxt++;
  }
}

console.log('Nice');