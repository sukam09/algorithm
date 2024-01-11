/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  let a = nums1;
  let b = nums2;
  const total = a.length + b.length;
  const half = parseInt(total / 2);

  if (a.length > b.length) {
    [a, b] = [b, a];
  }

  let l = 0;
  let r = a.length - 1;

  const max = 10 ** 6;
  const min = -max;

  while (true) {
    let i = Math.floor((l + r) / 2);
    let j = half - i - 2;

    let al = i >= 0 ? a[i] : min;
    let ar = i + 1 < a.length ? a[i + 1] : max;
    let bl = j >= 0 ? b[j] : min;
    let br = j + 1 < b.length ? b[j + 1] : max;

    if (al <= br && bl <= ar) {
      if (total % 2 === 1) {
        return Math.min(ar, br);
      }
      return (Math.max(al, bl) + Math.min(ar, br)) / 2;
    } else if (al > br) {
      r = i - 1;
    } else {
      l = i + 1;
    }
  }
};
