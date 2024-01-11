/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  const n = nums.length;
  nums.sort((a, b) => a - b);
  const ans = [];
  const set = new Set();

  for (let i = 0; i < n; i++) {
    let st = i + 1;
    let en = n - 1;
    while (st < en) {
      const sum = nums[i] + nums[st] + nums[en];
      if (sum === 0) {
        const res = [nums[i], nums[st], nums[en]];
        set.add(res.join(','));
        st++;
      } else if (sum < 0) {
        st++;
      } else {
        en--;
      }
    }
  }

  for (const s of set) {
    ans.push(s.split(','));
  }

  return ans;
};
