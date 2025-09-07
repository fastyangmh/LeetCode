# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = node = ListNode()
        carry = 0

        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            val = n1 + n2 + carry
            carry = 1 if val >= 10 else 0
            val = val % 10

            node.next = ListNode(val)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
