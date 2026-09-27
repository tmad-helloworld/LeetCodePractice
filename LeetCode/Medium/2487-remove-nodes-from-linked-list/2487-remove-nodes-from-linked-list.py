# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Stack:
    def __init__(self):
        self.stack = []
        self.top = None
        self.head = None

    def push(self,node):
        self.stack.append(node)
    
    def pop(self):
        self.stack.pop()
     
    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0
class Solution:
    
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        stack = Stack()
        stack.push(head)
        max = head.val
        while head:
            if head.val > stack.peek().val:
                max = head.val
                while stack.isEmpty() == False and stack.peek().val < max:
                    stack.pop()
                stack.push(head)
            
            else:
                stack.push(head)
                
            
            head = head.next

        for i in range(0,stack.size()-1):
            stack.stack[i].next = stack.stack[i+1]

        return stack.stack[0]
            

        