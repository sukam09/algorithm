/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  let sz = 0;
  let cur = head;
  while (cur !== null) {
    sz++;
    cur = cur.next;
  }

  const idx = sz - n;

  if (idx === 0) {
    return head.next;
  } else {
    let cur = head;
    let i = 0;
    while (cur !== null) {
      if (i === idx - 1) {
        cur.next = cur.next.next;
        break;
      }
      cur = cur.next;
      i++;
    }
    return head;
  }
};
