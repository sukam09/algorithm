/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  const arr1 = [];
  const arr2 = [];

  let cur = list1;
  while (cur !== null) {
    arr1.push(cur.val);
    cur = cur.next;
  }
  cur = list2;
  while (cur !== null) {
    arr2.push(cur.val);
    cur = cur.next;
  }

  const arr = [...arr1, ...arr2];
  arr.sort((a, b) => a - b);

  console.log(arr);

  let prev;
  const dummy = new ListNode();
  prev = dummy;

  for (const val of arr) {
    const node = new ListNode();
    node.val = val;
    prev.next = node;
    prev = node;
  }

  return dummy.next;
};
