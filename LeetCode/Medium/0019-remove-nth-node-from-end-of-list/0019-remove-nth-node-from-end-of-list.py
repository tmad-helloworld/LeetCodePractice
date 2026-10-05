# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:   
        dummy = ListNode()
        current = head
        index = 0
        while current:
            index += 1
            current=current.next

        current = dummy
        left = index - n
        right = left + 1
        while head and right > 0:
            if left > 0:
                current.next = head
                current = current.next
                left -= 1
            if right > 0:
                right -= 1

            head=head.next

            
        if index == 1:
            return None

        if n == 1:
            head = None
            
        current.next = head

        return dummy.next
            
        
        