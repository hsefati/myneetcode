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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr_list1, curr_list2 = list1, list2

        curr_node = merged_root = ListNode()

        while curr_list1 and curr_list2:
            if curr_list1.val <= curr_list2.val:
                curr_node.next = ListNode(curr_list1.val)
                curr_list1 = curr_list1.next
            else:
                curr_node.next = ListNode(curr_list2.val)
                curr_list2 = curr_list2.next

            curr_node = curr_node.next

        while curr_list1:
            curr_node.next = ListNode(curr_list1.val)
            curr_list1 = curr_list1.next
            curr_node = curr_node.next

        while curr_list2:
            curr_node.next = ListNode(curr_list2.val)
            curr_list2 = curr_list2.next
            curr_node = curr_node.next

        return merged_root.next


if __name__ == "__main__":
    # Creating list1 = [1,2,4]
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    # Creating list2 = [1,3,5]
    list2 = ListNode(1)
    list2.next = ListNode(2)
    # list2.next.next = ListNode(5)
    test = Solution()
    print_linked_list(test.mergeTwoLists(None, list2))
