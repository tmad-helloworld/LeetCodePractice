# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        current = dummy
        
        if head:
            
            while head:
                
                if head.next:
                    if head.next.next:
                        temp = head.next.next
                    else:
                        temp = None

                    current.next = head.next
                    current.next.next = head
                    head.next = temp
                    
                    
                    current = current.next.next
                
               
                else:
                    current.next = head
                head = head.next

                
   

        return dummy.next
                
        
        