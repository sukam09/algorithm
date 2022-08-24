const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" "));

const n = Number(input[0][0]);
const stack = [];
let answer = "";

for (let i = 1; i <= n; i++) {
  const command = input[i];
  if (command.length > 1) {
    const item = Number(command[1]);
    stack.push(item);
  } else {
    const size = stack.length;
    switch (command[0]) {
      case "pop":
        answer += size === 0 ? -1 : stack.pop();
        break;
      case "size":
        answer += size;
        break;
      case "empty":
        answer += size === 0 ? 1 : 0;
        break;
      case "top":
        answer += size === 0 ? -1 : stack[size - 1];
        break;
    }
    answer += "\n";
  }
}

console.log(answer);
