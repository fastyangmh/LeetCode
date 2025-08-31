# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # method1
        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

        # # method2
        # dummy = ListNode(0, head)
        # length = 0

        # node = head
        # while node:
        #     node = node.next
        #     length += 1

        # node = dummy
        # for _ in range(length - n):
        #     node = node.next

        # node.next = node.next.next

        # return dummy.next
