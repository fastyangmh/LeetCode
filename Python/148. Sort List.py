# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # method1
        # def merge(l1, l2):
        #     dummy = curr = ListNode()

        #     while l1 and l2:
        #         if l1.val <= l2.val:
        #             curr.next, l1 = l1, l1.next
        #         else:
        #             curr.next, l2 = l2, l2.next

        #         curr = curr.next

        #     curr.next = l1 or l2

        #     return dummy.next

        # if not head or not head.next:
        #     return head

        # slow = fast = head
        # fast = fast.next

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # right = slow.next
        # slow.next = None

        # l1 = self.sortList(head)
        # l2 = self.sortList(right)

        # return merge(l1, l2)

        # method2
        if not head or not head.next:
            return head

        def split(head, size):
            if not head:
                return None

            for _ in range(size - 1):
                if head.next:
                    head = head.next
                else:
                    break

            second = head.next
            head.next = None

            return second

        def merge(l1, l2):
            dummy = tail = ListNode()

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next, l1 = l1, l1.next
                else:
                    tail.next, l2 = l2, l2.next

                tail = tail.next

            tail.next = l1 or l2

            while tail.next:
                tail = tail.next

            return dummy.next, tail

        curr = head
        n = 0

        while curr:
            n += 1
            curr = curr.next

        dummy = ListNode(next=head)
        size = 1

        while size < n:
            prev = dummy
            curr = dummy.next

            while curr:
                left = curr
                right = split(left, size)
                curr = split(right, size)

                merged_head, merged_tail = merge(left, right)

                prev.next = merged_head
                prev = merged_tail

            size *= 2

        return dummy.next
