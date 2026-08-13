# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        prev, curr = None, mid

        while curr:
            prev, curr.next, curr = curr, prev, curr.next

        left = head
        right = prev

        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
