const input = require('fs').readFileSync('/dev/stdin').toString().trim();
console.log(
  input.replace(/<[a-z0-9 ]+>|[a-z0-9]+/g, x => {
    if (x.startsWith('<')) {
      return x;
    } else {
      return [...x].reverse().join('');
    }
  }),
);
