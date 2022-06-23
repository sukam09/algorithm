class Heap {
  constructor(n) {
    this.heap = Array(n + 1).fill(0); // size is n + 1 because of dummy node
    this.size = 0;
  }

  push(num) {
    this.heap[++this.size] = num;
    let index = this.size;
    while (index > 1) {
      const parent = Math.floor(index / 2);
      if (this.heap[parent] <= this.heap[index]) {
        break;
      }
      [this.heap[parent], this.heap[index]] = [
        this.heap[index],
        this.heap[parent],
      ];
      index = parent;
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
      [this.heap[index], this.heap[minChild]] = [
        this.heap[minChild],
        this.heap[index],
      ];
      index = minChild;
    }
  }

  top() {
    return this.heap[1];
  }

  isEmpty() {
    return this.size === 0;
  }
}

// Test
const heap = new Heap(5);

for (let i = 5; i >= 1; i--) {
  heap.push(i);
  console.log(heap);
}

for (let i = 0; i < 5; i++) {
  console.log(heap.top());
  heap.pop();
  console.log(heap);
}
