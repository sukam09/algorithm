/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  let p1 = l1;
  const arr1 = [];
  while (p1 !== null) {
    arr1.push(p1.val);
    p1 = p1.next;
  }
  arr1.reverse();
  let a = 0;
  for (const x of arr1) {
    a = a * 10 + x;
  }
  let p2 = l2;
  const arr2 = [];
  while (p2 !== null) {
    arr2.push(p2.val);
    p2 = p2.next;
  }
  arr2.reverse();
  let b = 0;
  for (const x of arr2) {
    b = b * 10 + x;
  }
  const sum = a + b;
  const sumstr = sum.toString();
  let answer;
  let next = null;
  for (const x of sumstr) {
    const num = parseInt(x, 10);
    answer = new ListNode(num, next);
    next = answer;
  }
  return answer;
};
