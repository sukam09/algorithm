/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  const y = x.toString();
  let answer = '';
  let sign = 1;
  for (const yy of y) {
    if (yy === '-') {
      sign = -1;
    } else {
      answer += yy;
    }
  }
  answer = answer.split('').reverse().join('');
  answer = parseInt(sign * answer);
  const max = Math.pow(2, 31) - 1;
  const min = -Math.pow(2, 31);
  if (answer > max) {
    return 0;
  }
  if (answer < min) {
    return 0;
  }
  return answer;
};
