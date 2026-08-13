# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(next=head)

        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next

            a.next = b.next
            b.next = a
            prev.next = b

            prev = a

        return dummy.next
