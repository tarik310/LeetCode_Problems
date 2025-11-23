from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        # One of the lists might still have remaining nodes
        tail.next = list1 if list1 else list2
        
        return dummy.next


# Example usage:
solution = Solution()
# Creating linked lists for testing: 1 -> 3 -> 5 and 2 -> 4 -> 6
list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))
merged_head = solution.mergeTwoLists(list1, list2)
# Print merged linked list
while merged_head:
    print(merged_head.val, end=" -> ")
    merged_head = merged_head.next
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 ->
