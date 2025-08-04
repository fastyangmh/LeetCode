# import
from typing import Optional


# class
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Floyd's Tortoise and Hare
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not isinstance(head, ListNode):
            return False

        seen = []
        stacks = [head]

        while stacks:
            stack = stacks.pop()
            hash_val = hash(stack)

            if hash_val in seen:
                return True
            else:
                seen.append(hash_val)

            if stack.next is not None:
                stacks.append(stack.next)

        return False


# def
def list2linkedlist(nums: list[int], pos: int) -> ListNode:
    non_linked_list = [ListNode(x) for x in nums]

    root = non_linked_list[0]

    for node in non_linked_list[1:]:
        root.next = node  # type: ignore
        root = node

    root.next = non_linked_list[pos] if pos >= 0 else None  # type: ignore

    return non_linked_list[0]


if __name__ == "__main__":
    # Example 1:
    head = [3, 2, 0, -4]
    pos = 1
    assert Solution().hasCycle(list2linkedlist(head, pos)) is True, Solution().hasCycle(
        list2linkedlist(head, pos)
    )

    # Example 2:
    head = [1, 2]
    pos = 0
    assert Solution().hasCycle(list2linkedlist(head, pos)) is True, Solution().hasCycle(
        list2linkedlist(head, pos)
    )

    # Example 3:
    head = [1]
    pos = -1
    assert Solution().hasCycle(list2linkedlist(head, pos)) is False, (
        Solution().hasCycle(list2linkedlist(head, pos))
    )
