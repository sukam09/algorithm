/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function (nums, target) {
  const n = nums.length;
  const ans = [];
  nums.sort((a, b) => a - b);
  const set = new Set();

  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      let st = j + 1;
      let en = n - 1;

      while (st < en) {
        const sum = nums[i] + nums[j] + nums[st] + nums[en];
        const res = [nums[i], nums[j], nums[st], nums[en]];
        if (sum === target) {
          set.add(res.join(','));
          st++;
        } else if (sum < target) {
          st++;
        } else {
          en--;
        }
      }
    }
  }

  for (const s of set) {
    ans.push(s.split(','));
  }

  return ans;
};
