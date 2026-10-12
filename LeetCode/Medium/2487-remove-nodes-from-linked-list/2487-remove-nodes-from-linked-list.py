# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        highest = stack.pop()
        current = ListNode(highest)
        while len(stack) > 0:
            temp_val = stack.pop()
            if temp_val < highest:
                continue
            else:
                highest = temp_val
                temp_node = ListNode(highest)
                temp_node.next = current
                current = temp_node
                
        return current
            
        
            
            
            