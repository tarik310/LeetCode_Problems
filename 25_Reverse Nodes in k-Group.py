from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Function to check if there are k nodes ahead
        def hasKNodes(node, k):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k
        
        dummy = ListNode(0)
        dummy.next = head
        
        groupPrev = dummy
        
        while True:
            # Check if there are k nodes to reverse
            if not hasKNodes(groupPrev.next, k):
                break
            
            # Reverse k nodes
            prev = None
            curr = groupPrev.next
            tail = curr   # tail will become the end of the reversed group
            
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # Connect reversed group back to the list
            groupPrev.next = prev
            tail.next = curr
            
            # Move groupPrev to the end of the reversed group
            groupPrev = tail
        
        return dummy.next




# Example usage:
solution = Solution()
# Creating linked list for testing: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
reversed_head = solution.reverseKGroup(head, k)
# Print reversed linked list
while reversed_head:
    print(reversed_head.val, end=" -> ")
    reversed_head = reversed_head.next
# Output: 2 -> 1 -> 4 -> 3 -> 5 ->