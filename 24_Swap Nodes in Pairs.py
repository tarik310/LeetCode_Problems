from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            first = head
            second = head.next

            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first

            # Move pointers
            prev = first
            head = first.next

        return dummy.next


# Example usage:
solution = Solution()
# Creating linked list for testing: 1 -> 2 -> 3 -> 4
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
swapped_head = solution.swapPairs(head)
# Print swapped linked list
while swapped_head:
    print(swapped_head.val, end=" -> ")
    swapped_head = swapped_head.next
# Output: 2 -> 1 -> 4 -> 3 ->