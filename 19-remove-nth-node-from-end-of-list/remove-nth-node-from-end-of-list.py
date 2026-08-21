# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        a = 0
        fast = head
        while fast:
            a += 1
            fast = fast.next
        slow = dummy
        for _ in range(a - n):
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next