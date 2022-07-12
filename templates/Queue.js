class Queue {
  constructor() {
    this.queue = [];
    this.head = 0;
    this.tail = 0;
  }

  push(item) {
    this.queue[this.tail++] = item;
  }

  pop() {
    return this.queue[this.head++];
  }

  isEmpty() {
    return this.tail - this.head === 0;
  }
}
