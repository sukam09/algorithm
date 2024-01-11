/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
  const result = [...Array(1000)].map(() => []);
  let row = 0;
  let dir = 0;
  for (const x of s) {
    result[row].push(x);
    if (row === numRows - 1) {
      dir = 1;
    } else if (row === 0) {
      dir = 0;
    }

    if (dir === 0) {
      row++;
    } else {
      row--;
    }
  }
  let answer = '';
  for (let i = 0; i < numRows; i++) {
    answer += result[i].join('');
  }
  return answer;
};
