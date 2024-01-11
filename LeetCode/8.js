/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function (s) {
  let answer = '';
  let sign = 1;
  const max = Math.pow(2, 31) - 1;
  const min = -Math.pow(2, 31);

  function isdigit(c) {
    return (c >= '0' && c <= '9') || c === '.';
  }

  function issign(c) {
    return c === '+' || c === '-';
  }

  let isread = false;

  for (let i = 0; i < s.length; i++) {
    if (!isread && s[i] === ' ') {
      continue;
    }
    // 소수점 포함
    if (isdigit(s[i])) {
      answer += s[i];
    } else {
      // 일단 숫자가 아님
      if (!isread) {
        if (s[i] === '+') {
          sign = 1;
        } else if (s[i] === '-') {
          sign = -1;
        } else {
          break;
        }
      } else {
        break;
      }
    }
    isread = true;
  }
  if (answer === '') {
    return 0;
  }
  answer = parseFloat(answer);
  if (sign === -1) {
    answer = -answer;
  }
  if (answer > max) {
    answer = max;
  } else if (answer < min) {
    answer = min;
  }
  return answer;
};
