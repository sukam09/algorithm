/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  let ans = '';

  for (let k = 0; k < 200; k++) {
    let target = strs[0][k];
    for (let i = 0; i < strs.length; i++) {
      if (strs[i][k] !== target) {
        return ans;
      }
    }
    ans += target;
  }

  return ans;
};
