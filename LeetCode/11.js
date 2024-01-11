/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let ans = 0;
  let st = 0;
  let en = height.length - 1;
  while (st < en) {
    ans = Math.max(ans, Math.min(height[st], height[en]) * (en - st));
    if (height[st] < height[en]) {
      st++;
    } else {
      en--;
    }
  }

  return ans;
};
