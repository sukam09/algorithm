/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
  let arr = [];
  let cur;
  for (const list of lists) {
    cur = list;
    while (cur !== null) {
      arr.push(cur.val);
      cur = cur.next;
    }
  }
  arr.sort((a, b) => a - b);
  const dummy = new ListNode();
  let prev = dummy;
  for (const val of arr) {
    const node = new ListNode();
    node.val = val;
    prev.next = node;
    prev = node;
  }
  return dummy.next;
};
