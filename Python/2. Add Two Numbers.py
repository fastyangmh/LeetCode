from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_number = self.get_number(listnode=l1)
        l2_number = self.get_number(listnode=l2)
        s = l1_number+l2_number
        ans = ListNode()
        ptr = ans
        while s > 0:
            ptr.val = s % 10
            s = s//10
            if s > 0:
                ptr.next = ListNode()
                ptr = ptr.next
        return ans

    def get_number(self, listnode):
        count = 0
        number = 0
        while listnode:
            number += listnode.val*(10**count)
            count += 1
            listnode = listnode.next
        return number
