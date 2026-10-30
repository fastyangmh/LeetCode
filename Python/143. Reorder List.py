# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        prev, curr = None, mid

        while curr:
            prev, curr.next, curr = curr, prev, curr.next

        l1 = head
        l2 = prev

        while l2:
            tmp1 = l1.next
            tmp2 = l2.next

            l1.next = l2
            l2.next = tmp1

            l1 = tmp1
            l2 = tmp2
