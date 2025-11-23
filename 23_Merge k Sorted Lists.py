from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0:
            return None
        
        # Keep merging lists two at a time
        while len(lists) > 1:
            merged = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwo(l1, l2))
            
            lists = merged
        
        return lists[0]

    # Merge two sorted linked lists
    def mergeTwo(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 if l1 else l2
        return dummy.next



# Example usage:
solution = Solution()
# Creating linked lists for testing
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
merged_head = solution.mergeKLists([list1, list2, list3])
# Print merged linked list
while merged_head:
    print(merged_head.val, end=" -> ")
    merged_head = merged_head.next

# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 ->
