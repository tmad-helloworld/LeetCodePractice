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
            
        counter = -1
        
        highest = stack.pop()
        length = len(stack)
        current = ListNode(highest)
        while -(counter) <= length:
            if stack[counter] <  highest:
                pass
                
            
            else:
                temp = ListNode(stack[counter])
                temp.next = current
                current = temp
                highest = stack[counter]

            counter = counter -1

        return current
                

       