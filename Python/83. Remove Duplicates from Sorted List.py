# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # method1
        # dummy = slow = fast = ListNode(val=None, next=head)
        # fast = fast.next

        # while fast:
        #     if slow.val != fast.val:
        #         slow.next = fast
        #         slow = slow.next
        #     fast = fast.next
        # slow.next = None

        # return dummy.next

        # method2
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
