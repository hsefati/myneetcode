from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __eq__(self, other):
    #     if not isinstance(other, ListNode):
    #         return False
    #     return self.val == other.val and self.next == other.next


def print_linked_list(head: ListNode) -> None:
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    # Creating list1 = [1,2,3,4,2]
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)
    list1.next.next.next = ListNode(4)
    list1.next.next.next.next = ListNode(2)

    test = Solution()
    print(test.hasCycle(list1))
