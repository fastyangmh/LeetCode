# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iteratively
        prev, curr = None, head

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        return prev

        # # recursively
        # if not head or head.next is None:
        #     return head

        # new_head = self.reverseList(head.next)

        # head.next.next = head
        # head.next = None

        # return new_head
