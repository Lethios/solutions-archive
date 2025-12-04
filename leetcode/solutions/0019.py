# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        len_n = 0

        while current:
            len_n += 1
            current = current.next

        if n == len_n:
            return head.next

        current = head
        for _ in range(len_n - n - 1):
            current = current.next
        current.next = current.next.next

        return head
