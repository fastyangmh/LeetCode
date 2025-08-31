# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # method1
        vals = []

        node = head

        while node:
            vals.append(node.val)
            node = node.next

        left, right = 0, len(vals) - 1

        while left < right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1

        return True

        # # method2
        # if not head or not head.next:
        #     return True

        # slow = fast = head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # prev, curr = None, slow

        # while curr:
        #     curr.next, prev, curr = prev, curr, curr.next

        # left, right = head, prev

        # while left and right:
        #     if left.val != right.val:
        #         return False
        #     left = left.next
        #     right = right.next

        # return True
