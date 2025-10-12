import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # # method1 mine
        # dummy = ListNode()

        # while lists:
        #     head = dummy

        #     nodes = lists.pop()

        #     while nodes:
        #         while head.next and head.next.val < nodes.val:
        #             head = head.next

        #         tmp = head.next
        #         head.next = nodes
        #         nodes = nodes.next
        #         head.next.next = tmp

        # return dummy.next

        # # method2
        # heap = []

        # for idx, node in enumerate(lists):
        #     if not node:
        #         continue

        #     heapq.heappush(heap, (node.val, idx, node))

        # dummy = current = ListNode()

        # while heap:
        #     val, list_idx, node = heapq.heappop(heap)
        #     current.next = node
        #     current = current.next

        #     if node.next:
        #         heapq.heappush(heap, (node.next.val, list_idx, node.next))

        # return dummy.next

        # method3
        if not lists:
            return None

        def merge_lists(l1, l2):
            dummy = curr = ListNode()

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next, l1 = l1, l1.next
                else:
                    curr.next, l2 = l2, l2.next
                curr = curr.next

            curr.next = l1 or l2

            return dummy.next

        while len(lists) > 1:
            merged = []

            for list_idx in range(0, len(lists), 2):
                l1 = lists[list_idx]
                l2 = lists[list_idx + 1] if list_idx + 1 < len(lists) else None
                merged.append(merge_lists(l1, l2))

            lists = merged

        return lists[0]
