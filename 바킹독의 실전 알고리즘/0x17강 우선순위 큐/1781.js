class MinHeap {
  constructor() {
    this.data = [];
    this.size = 0;
  }

  push(x) {
    this.data[++this.size] = x;
    let index = this.size;
    while (index > 1) {
      const parentIndex = Math.floor(index / 2);
      if (this.data[parentIndex] <= this.data[index]) {
        break;
      }
      this.swap(parentIndex, index);
      index = parentIndex;
    }
  }

  top() {
    return this.data[1];
  }

  pop() {
    this.data[1] = this.data[this.size--];
    let index = 1;
    while (2 * index <= this.size) {
      const leftChild = 2 * index;
      const rightChild = 2 * index + 1;
      let minChild = leftChild;
      if (rightChild <= this.size && this.data[rightChild] < this.data[leftChild]) {
        minChild = rightChild;
      }
      if (this.data[index] <= this.data[minChild]) {
        break;
      }
      this.swap(index, minChild);
      index = minChild;
    }
  }

  swap(a, b) {
    [this.data[a], this.data[b]] = [this.data[b], this.data[a]];
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
  .map(line => line.split(' ').map(Number));

const n = input[0][0];
const arr = [];
for (let i = 1; i <= n; i++) {
  const [deadline, cupRamen] = input[i];
  arr.push([deadline, cupRamen]);
}
arr.sort((a, b) => (a[0] === b[0] ? b[1] - a[1] : a[0] - b[0]));

const heap = new MinHeap();
for (const [deadline, cupRamen] of arr) {
  if (heap.size < deadline) {
    heap.push(cupRamen);
  } else if (cupRamen > heap.top()) {
    heap.pop();
    heap.push(cupRamen);
  }
}

let answer = 0;
for (let i = 1; i <= heap.size; i++) {
  answer += heap.data[i];
}
console.log(answer);
