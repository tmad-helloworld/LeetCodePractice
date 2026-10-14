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
        temp_node = None
        right_node = None
        while counter <= right and head:
            if counter < left:
                current.next = head
                current = current.next
                head = head.next
                counter += 1
                continue
            if counter == left:
                if head.next:
                    temp_node = head.next
                right_most = head
                right_node = head
                head = temp_node

            else:
                temp_node = head.next
                head.next = right_node
                right_node = head
                head = temp_node
                
                

                
            
            
            counter+=1

        current.next = right_node
        right_most.next = head

        return dummy.next