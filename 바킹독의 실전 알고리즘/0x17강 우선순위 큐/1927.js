class Heap {
  constructor(n) {
    this.heap = Array(n + 1).fill(0); // size is n + 1 because of dummy node
    this.size = 0;
  }

  push(num) {
    this.heap[++this.size] = num;
    let index = this.size;
    while (index > 1) {
      const parentIndex = Math.floor(index / 2);
      if (this.heap[parentIndex] <= this.heap[index]) {
        break;
      }
      this.swap(parentIndex, index);
      index = parentIndex;
    }
  }

  pop() {
    this.heap[1] = this.heap[this.size];
    this.heap[this.size--] = 0;
    let index = 1;
    while (2 * index <= this.size) {
      const leftChild = 2 * index;
      const rightChild = 2 * index + 1;
      let minChild = leftChild;
      if (
        rightChild <= this.size &&
        this.heap[rightChild] < this.heap[leftChild]
      ) {
        minChild = rightChild;
      }
      if (this.heap[index] <= this.heap[minChild]) {
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

const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map((x) => +x);
const n = input[0];
const heap = new Heap(n);
let answer = '';

for (let i = 1; i <= n; i++) {
  const num = input[i];
  if (num === 0) {
    if (heap.isEmpty()) {
      answer += '0\n';
    } else {
      answer += `${heap.top()}\n`;
      heap.pop();
    }
  } else {
    heap.push(num);
  }
}

console.log(answer);
