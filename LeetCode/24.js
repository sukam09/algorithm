/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function (head) {
  let sz = 0;
  let cur = head;
  while (cur !== null) {
    sz++;
    cur = cur.next;
    if (sz === 2) {
      break;
    }
  }

  if (sz < 2) {
    return head;
  }

  const dummy = new ListNode();

  let p, q, next;
  let lost = dummy;
  cur = head;

  while (cur !== null) {
    p = cur;
    q = cur.next;

    if (q === null) {
      lost.next = p;
      break;
    }

    next = q.next;
    q.next = p;
    p.next = null;
    lost.next = q;
    lost = p;

    cur = next;
  }

  return dummy.next;
};
