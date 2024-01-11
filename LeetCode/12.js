/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
  const n = num.toString().padStart(4, '0');

  const digits = 'MCXI';
  const fiveDigits = ' DLV';

  let ans = '';

  for (let i = 0; i < 4; i++) {
    const m = parseInt(n[i]);

    if (m === 0) {
      continue;
    }

    if (m === 4) {
      ans += digits[i] + fiveDigits[i];
    } else if (m === 9) {
      ans += digits[i] + digits[i - 1];
    } else if (m <= 3) {
      ans += digits[i].repeat(m);
    } else {
      ans += fiveDigits[i] + digits[i].repeat(m - 5);
    }
  }

  return ans;
};
