import Heap from './heap.js';

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
