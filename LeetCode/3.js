/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  const set = new Set();
  let ans = 1;
  const n = s.length;
  let en = 0;
  set.add(s[0]);
  for (let st = 0; st < n; st++) {
    while (en < n - 1 && !set.has(s[en + 1])) {
      en++;
      set.add(s[en]);
    }
    ans = Math.max(ans, en - st + 1);
    set.delete(s[st]);
  }
  return ans;
};
