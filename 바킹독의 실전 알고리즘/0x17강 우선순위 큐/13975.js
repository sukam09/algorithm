class MinHeap {
  constructor() {
    this.data = [];
    this.size = 0;
  }

  push(item) {
    this.data[++this.size] = item;
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
      if (
        rightChild <= this.size &&
        this.data[rightChild] < this.data[leftChild]
      ) {
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

const solution = (files) => {
  const heap = new MinHeap();
  let result = 0;
  for (const file of files) {
    heap.push(file);
  }
  while (heap.size >= 2) {
    const a = heap.top();
    heap.pop();
    const b = heap.top();
    heap.pop();
    result += a + b;
    heap.push(a + b);
  }
  return result;
};

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

const n = input[0][0];
let answer = "";
for (let i = 1; i <= n; i++) {
  const files = input[i * 2];
  answer += solution(files) + "\n";
}

console.log(answer);
