# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        current = dummy
        head = head.next
        sum = 0
        while head:
            if head.val == 0:
                current.next = ListNode(sum)
                current = current.next
                head = head.next
                sum = 0
                continue

            else:
                sum = sum + head.val
            
            head = head.next

        return dummy.next
        