/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const stack = [];
  const pair = new Map([
    [')', '('],
    ['}', '{'],
    [']', '['],
  ]);

  for (const x of s) {
    if ('({['.includes(x)) {
      stack.push(x);
    } else {
      if (stack.length === 0) {
        return false;
      }

      const top = stack.at(-1);
      if (pair.get(x) === top) {
        stack.pop();
      } else {
        return false;
      }
    }
  }

  return stack.length === 0;
};
