# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        sum = 0
        dummy = ListNode()
        current = dummy
        pointer = None
        
        while head:
            if head.val == 0:
                if sum == 0:
                    head = head.next
                    continue
                    
                else:
                    current.next = ListNode(sum)
                    sum = 0
                    current = current.next
            
            else:
                sum = sum + head.val
            
            
            head = head.next

        return dummy.next
                    
        