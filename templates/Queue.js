class Queue {
  constructor() {
    this.queue = [];
    this.head = 0;
    this.tail = 0;
  }

  push(x) {
    this.queue[this.tail++] = x;
  }

  pop() {
    return this.queue[this.head++];
  }

  isEmpty() {
    return this.tail - this.head === 0;
  }
}
