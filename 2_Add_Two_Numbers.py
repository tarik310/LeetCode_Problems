# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)  # Start with a dummy node to handle the result linked list
        current = dummy_head
        carry = 0  # Initialize carry to 0
        
        while l1 is not None or l2 is not None or carry:
            # Extract values from the current nodes of l1 and l2, or 0 if they've been exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of current digits plus carry
            total = val1 + val2 + carry
            
            # Update carry for next iteration (1 if total is 10 or greater)
            carry = total // 10
            
            # Create a new node for the current digit (total modulo 10)
            current.next = ListNode(total % 10)
            
            # Move current to the next node in the result list
            current = current.next
            
            # Move to the next nodes in l1 and l2 if possible
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the next of dummy_head to exclude the initial dummy node
        return dummy_head.next

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy_head = ListNode()
    current = dummy_head
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy_head.next

# Helper function to print the linked list
def print_linked_list(l):
    result = []
    while l:
        result.append(str(l.val))
        l = l.next
    print("->".join(result))

# Test cases
solution = Solution()

# Example 1: l1 = [2,4,3], l2 = [5,6,4]
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = solution.addTwoNumbers(l1, l2)
print("Example 1: ")
print_linked_list(result)  # Expected output: 7->0->8

# Example 2: l1 = [0], l2 = [0]
l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = solution.addTwoNumbers(l1, l2)
print("Example 2: ")
print_linked_list(result)  # Expected output: 0

# Example 3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = solution.addTwoNumbers(l1, l2)
print("Example 3: ")
print_linked_list(result)  # Expected output: 8->9->9->9->0->0->0->1
