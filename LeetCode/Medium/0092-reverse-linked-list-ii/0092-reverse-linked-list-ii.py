# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode()
        current = dummy
        counter = 1
        temp = None
        right_most = None
        right_node = None
        while head and counter <= right:
            
            if (counter >= left) and (counter <= right):
                
                temp = head.next
                
                head.next = right_node
                right_node = head
                if counter == left:
                    right_most = right_node
                head = temp
            
            elif(counter < left):
                current.next = head
                current = current.next
                head = head.next

            
                

            counter += 1

        current.next = right_node
        right_most.next = head
            

        
        return dummy.next
                