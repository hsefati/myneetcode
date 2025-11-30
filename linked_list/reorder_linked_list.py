from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(head: ListNode) -> None:
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


if __name__ == "__main__":
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(8)
    # head.next.next.next.next = ListNode(4)
    # head.next.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next.next = ListNode(6)

    test = Solution()
    print_linked_list(test.reorderList(head))
