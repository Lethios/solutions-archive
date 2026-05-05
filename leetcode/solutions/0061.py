# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head

        n = 1
        last = head
        while last.next is not None:
            n += 1
            last = last.next

        if n == 1:
            return head

        k %= n
        if k == 0:
            return head

        curr = head
        for _ in range(n - k - 1):
            curr = curr.next

        temp = curr.next
        curr.next = None
        last.next = head

        return temp
