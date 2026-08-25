# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        my_low = ListNode(0)
        my_high = ListNode(0)
        low = my_low
        high = my_high
        while head:
            if head.val < x:
                low.next = head
                low = low.next
            else:
                high.next = head
                high = high.next
            head = head.next
        high.next = None
        low.next = my_high.next
        return my_low.next