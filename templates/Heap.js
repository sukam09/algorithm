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

  pop() {
    const item = this.heap[1];
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
    return item;
  }

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }

  isEmpty() {
    return this.size === 0;
  }
}
