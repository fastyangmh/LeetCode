# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_value = str(l1.val)
        z = l1.next
        while z != None:
            l1_value += str(z.val)
            z = z.next
        l2_value = str(l2.val)
        z = l2.next
        while z != None:
            l2_value += str(z.val)
            z = z.next
        sum_value = str(int(l1_value)+int(l2_value))
        ans = ListNode(val=int(sum_value[-1]))
        for v in sum_value[:-1][::-1]:
            z = ListNode(val=v, next=ans)
            ans = z
        return ans


if __name__ == "__main__":
    l1 = ListNode(val=7, next=ListNode(
        val=2, next=ListNode(val=4, next=ListNode(val=3, next=None))))
    l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
    print(Solution().addTwoNumbers(l1=l1, l2=l2))
