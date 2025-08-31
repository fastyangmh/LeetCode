# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # method1
        node.val = node.next.val
        node.next = node.next.next

        # # method2
        # slow, fast = node, node.next

        # while slow.next is not None and fast.next is not None:
        #     slow.val = slow.next.val
        #     slow = slow.next
        #     fast = fast.next

        # slow.val = fast.val
        # slow.next = None
