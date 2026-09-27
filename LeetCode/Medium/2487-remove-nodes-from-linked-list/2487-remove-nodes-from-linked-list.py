# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        stack = []
        stack.append(head)
        max = head.val
        while head:
            if head.val > stack[-1].val:
                max = head.val
                while len(stack) != 0 and stack[-1].val < max:
                    stack.pop()
                stack.append(head)
            
            else:
                stack.append(head)
                
            
            head = head.next

        for i in range(0,len(stack)-1):
            stack[i].next = stack[i+1]

        return stack[0]
            

        