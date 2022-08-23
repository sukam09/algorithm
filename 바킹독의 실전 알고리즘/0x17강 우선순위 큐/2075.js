class Heap {
  constructor() {
    this.heap = [];
    this.size = 0;
  }

  push(item) {
    this.heap[++this.size] = item;
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

  top() {
    return this.heap[1];
  }

  pop() {
    this.heap[1] = this.heap[this.size--];
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

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }

  isEmpty() {
    return this.size === 0;
  }
}

// 이 문제는 메모리 제한 때문에 fs 모듈을 이용해서 푸는 것이 불가능함
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let count = -1;
let n = 0;
const heap = new Heap();

rl.on("line", (line) => {
  if (count === -1) {
    count = Number(line);
    n = count;
    return;
  }
  line.split(" ").forEach((value) => {
    heap.push(Number(value));
    if (heap.size > n) {
      heap.pop();
    }
  });
  count--;
  if (count === 0) {
    rl.close();
  }
}).on("close", () => {
  console.log(heap.top());
  process.exit();
});
