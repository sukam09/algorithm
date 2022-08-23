class Heap {
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

class MaxHeap {
  constructor() {
    this.data = [];
    this.size = 0;
  }

  push(item) {
    this.data[++this.size] = item;
    let index = this.size;
    while (index > 1) {
      const parentIndex = Math.floor(index / 2);
      if (this.data[parentIndex] >= this.data[index]) {
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
      let maxChild = leftChild;
      if (
        rightChild <= this.size &&
        this.data[rightChild] > this.data[leftChild]
      ) {
        maxChild = rightChild;
      }
      if (this.data[index] >= this.data[maxChild]) {
        break;
      }
      this.swap(index, maxChild);
      index = maxChild;
    }
  }

  swap(a, b) {
    [this.data[a], this.data[b]] = [this.data[b], this.data[a]];
  }

  isEmpty() {
    return this.size === 0;
  }
}
