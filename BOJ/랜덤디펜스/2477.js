const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const k = +input[0];
const arr = input.slice(1).map(x => x.split(' ').map(x => +x));

let hmax = 0;
let vmax = 0;
let hidx = -1;
let vidx = -1;

for (let i = 0; i < arr.length; i++) {
  const [x, y] = arr[i];
  if (x <= 2) {
    if (y > hmax) {
      hmax = y;
      hidx = i;
    }
  } else {
    if (y > vmax) {
      vmax = y;
      vidx = i;
    }
  }
}

let st;
if (Math.abs(hidx - vidx) === 1) {
  st = Math.max(hidx, vidx);
} else {
  st = Math.min(hidx, vidx);
}
const st1 = (st + 2) % arr.length;
const st2 = (st1 + 1) % arr.length;
const min1 = arr[st1][1];
const min2 = arr[st2][1];

console.log(k * (hmax * vmax - min1 * min2));
