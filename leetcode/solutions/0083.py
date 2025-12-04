# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = scout = head

        while scout and scout.next:
            scout = scout.next
            if scout.val != current.val:
                current.next = scout
                current = scout

        if scout != current:
            current.next = None

        return head
