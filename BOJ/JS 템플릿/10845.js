class Queue {
  constructor() {
    this.front = 0;
    this.rear = 0;
    this.q = [];
  }

  push(x) {
    this.q[this.rear++] = x;
  }

  top() {
    return this.q[this.front];
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
const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const n = Number(input[0]);
let ans = '';
for (let i = 1; i <= n; i++) {
  const cmd = input[i].split(' ');
  if (cmd.length === 2) {
    const x = Number(cmd[1]);
    q.push(x);
  } else if (cmd[0] === 'pop') {
    if (q.empty()) {
      ans += -1 + '\n';
    } else {
      ans += q.top() + '\n';
      q.pop();
    }
  } else if (cmd[0] === 'size') {
    ans += q.size() + '\n';
  } else if (cmd[0] === 'empty') {
    ans += +q.empty() + '\n';
  } else if (cmd[0] === 'front') {
    if (q.empty()) {
      ans += -1 + '\n';
    } else {
      ans += q.top() + '\n';
    }
  } else {
    if (q.empty()) {
      ans += -1 + '\n';
    } else {
      ans += q.q[q.rear - 1] + '\n';
    }
  }
}
console.log(ans);
