class Queue {
  constructor() {
    this.dat = [];
    this.head = 0;
    this.tail = 0;
  }

  push(x) {
    this.dat[this.tail++] = x;
  }

  pop() {
    this.head++;
  }

  front() {
    return this.dat[this.head];
  }

  rear() {
    return this.dat[this.tail - 1];
  }

  empty() {
    return this.head === this.tail;
  }
}

// l, r 함수를 string 연산으로 구현할 경우 TLE
const d = cur => (2 * cur) % 10000;
const s = cur => (cur === 0 ? 9999 : cur - 1);
const l = cur => (cur % 1000) * 10 + parseInt(cur / 1000);
const r = cur => (cur % 10) * 1000 + parseInt(cur / 10);

const func = [d, s, l, r];
const route = 'DSLR';

const solve = (a, b) => {
  const dist = Array(10000).fill('');
  const q = new Queue();
  q.push(a);
  while (!q.empty()) {
    const cur = q.front();
    q.pop();
    if (cur === b) {
      ans += dist[cur] + '\n';
      return;
    }
    for (let dir = 0; dir < 4; dir++) {
      const nxt = func[dir](cur);
      // a는 이미 방문한 것으로 간주
      if (nxt === a || dist[nxt] !== '') {
        continue;
      }
      dist[nxt] = dist[cur] + route[dir];
      q.push(nxt);
    }
  }
};

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let ans = '';
for (let i = 1; i < input.length; i++) {
  const [a, b] = input[i].split(' ').map(Number);
  solve(a, b);
}
console.log(ans);
