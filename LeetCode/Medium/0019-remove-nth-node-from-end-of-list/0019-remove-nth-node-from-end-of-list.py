# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        indexes = 0
        check = head
        while check:
            indexes += 1
            check = check.next

        if indexes == 1:
            return None
        
        forward_stop = indexes - n
        backward_stop = forward_stop + 1
        fast_pointer = head
        
        dummy = ListNode()
        current = dummy
        
        while head and backward_stop > 0:
            if forward_stop > 0:
                current.next = head
                current = current.next
                forward_stop -= 1

            if backward_stop > 0:
                head = head.next
                backward_stop -= 1

            else:
                break
            
        if n == 1:
            current.next = None
            
        else:
            current.next = head

        return dummy.next
                
            
            