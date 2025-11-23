from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        
        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both pointers until fast reaches the last node
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        # Delete the nth node from the end
        slow.next = slow.next.next
        
        return dummy.next


# Example usage:
solution = Solution()
example_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new_head = solution.removeNthFromEnd(example_list, 2)
# Print the modified list
current = new_head
while current:
    print(current.val, end=" -> " if current.next else "")
    current = current.next
# Output: 1 -> 2 -> 3 -> 5

