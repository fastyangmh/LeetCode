# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        n = 1
        node = head

        while node.next:
            n += 1
            node = node.next

        node.next = head
        k %= n

        for _ in range(n - k):
            node = node.next

        new_head = node.next
        node.next = None

        return new_head
