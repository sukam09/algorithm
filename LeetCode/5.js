/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  const dp = [...Array(s.length)].map(() => Array(s.length).fill(0));
  // i: 간격, j: 시작 인덱스
  for (let i = 0; i < s.length; i++) {
    for (let j = 0; j < s.length - i; j++) {
      if (i === 0) {
        dp[j][j] = 1;
      } else if (i === 1) {
        if (s[j] === s[j + 1]) {
          dp[j][j + 1] = 1;
        }
      } else {
        const start = j;
        const end = j + i;
        dp[start][end] = dp[start + 1][end - 1] === 1 && s[start] === s[end] ? 1 : 0;
      }
    }
  }
  for (let i = s.length - 1; i >= 0; i--) {
    for (let j = 0; j < s.length; j++) {
      if (dp[j][j + i] === 1) {
        return s.substring(j, j + i + 1);
      }
    }
  }
};
