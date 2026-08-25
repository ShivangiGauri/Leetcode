# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_list = []
        curr = head
        while curr:
            my_list.append(curr.val)
            curr = curr.next
        my_list.sort()
        curr = head
        i = 0
        while curr:
            curr.val = my_list[i]
            i += 1
            curr = curr.next
        return head