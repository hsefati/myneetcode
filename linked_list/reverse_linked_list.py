from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print_linked_list(self, head):
        current = head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
            keep = curr.next
            curr.next = prev
            prev = curr
            curr = keep

        return prev


if __name__ == "__main__":
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    test = Solution()
    test.print_linked_list(test.reverseList(head))
