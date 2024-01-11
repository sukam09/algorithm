/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function (nums, target) {
  const n = nums.length;
  let sum = 0;
  let diff = 99999;
  let ans = 0;
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      for (let k = j + 1; k < n; k++) {
        sum = nums[i] + nums[j] + nums[k];
        const cur = Math.abs(sum - target);
        if (cur < diff) {
          ans = sum;
          diff = cur;
        }
      }
    }
  }
  return ans;
};
