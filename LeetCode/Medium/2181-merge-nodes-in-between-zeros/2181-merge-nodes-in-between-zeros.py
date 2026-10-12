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
                temp = ListNode(sum)
                current.next = temp
                current = current.next
                sum = 0

            else:
                sum += head.val

            head=head.next

        return dummy.next