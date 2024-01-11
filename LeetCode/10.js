/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function (s, p) {
  s = ' ' + s;
  p = ' ' + p;

  const sl = s.length;
  const pl = p.length;
  const dp = [...Array(sl)].map(() => Array(pl).fill(0));

  dp[0][0] = 1;
  for (let j = 1; j < pl; j++) {
    if (p[j] === '*') {
      dp[0][j] = dp[0].at(j - 2);
    }
  }
  for (let i = 1; i < sl; i++) {
    for (let j = 1; j < pl; j++) {
      if (`${s[i]}.`.includes(p[j])) {
        dp[i][j] = dp[i - 1][j - 1];
      } else if (p[j] === '*') {
        dp[i][j] = dp[i].at(j - 2) || (dp[i - 1][j] && +`${s[i]}.`.includes(p[j - 1]));
      }
    }
  }

  return dp[sl - 1][pl - 1];
};
