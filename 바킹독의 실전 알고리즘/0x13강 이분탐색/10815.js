const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

const cards = input[1];
const targets = input[3];

const cardSet = new Set();
for (const card of cards) {
  cardSet.add(card);
}

let answer = "";
for (const target of targets) {
  answer += (cardSet.has(target) ? 1 : 0) + " ";
}
console.log(answer);
