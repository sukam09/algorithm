class Heap {
  constructor(n) {
    this.heap = Array(n + 1).fill([0, 0]);
    this.size = 0;
  }

  push(node) {
    this.heap[++this.size] = node;
    let index = this.size;
    while (index > 1) {
      const parentIndex = Math.floor(index / 2);
      if (this.heap[parentIndex][0] <= this.heap[index][0]) {
        break;
      }
      this.swap(parentIndex, index);
      index = parentIndex;
    }
  }

  pop() {
    this.heap[1] = this.heap[this.size];
    this.heap[this.size--] = [0, 0];
    let index = 1;
    while (2 * index <= this.size) {
      const leftChild = 2 * index;
      const rightChild = 2 * index + 1;
      let minChild = leftChild;
      if (
        rightChild <= this.size &&
        this.heap[rightChild][0] < this.heap[leftChild][0]
      ) {
        minChild = rightChild;
      }
      if (this.heap[index][0] <= this.heap[minChild][0]) {
        break;
      }
      this.swap(index, minChild);
      index = minChild;
    }
  }

  top() {
    return this.heap[1];
  }

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }

  isEmpty() {
    return this.size === 0;
  }
}

const dijkstra = () => {
  const heap = new Heap(e);
  dists[k] = 0;
  heap.push([dists[k], k]);
  while (!heap.isEmpty()) {
    const [curDist, curNode] = heap.top();
    heap.pop();
    if (dists[curNode] != curDist) {
      continue;
    }
    for (let [nextDist, nextNode] of graph[curNode]) {
      if (dists[nextNode] <= dists[curNode] + nextDist) {
        continue;
      }
      dists[nextNode] = dists[curNode] + nextDist;
      heap.push([dists[nextNode], nextNode]);
    }
  }
};

const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');
const [v, e] = input[0].split(' ').map((x) => +x);
const k = parseInt(input[1]);
const dists = Array(v + 1).fill(Infinity);

// 아래 과정 대신 const graph = Array(v + 1).fill([])를 하면 push()할때마다 Array의 모든 element에서 삽입이 일어남 why?
// 얕은 복사가 일어나기 때문?
const graph = [];
for (let i = 0; i < v + 1; i++) {
  graph.push([]);
}
for (let i = 2; i < 2 + e; i++) {
  const [start, end, dist] = input[i].split(' ').map((x) => +x);
  graph[start].push([dist, end]);
}

dijkstra();
let answer = '';
for (let i = 1; i <= v; i++) {
  answer += dists[i] === Infinity ? 'INF' : dists[i];
  answer += '\n';
}
console.log(answer);
