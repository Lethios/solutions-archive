# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        if not head or not head.next:
            return head

        slow = mid = fast = dummy

        while fast.next and fast.next.next:
            mid = mid.next
            fast = fast.next.next
            temp = fast.next

            slow.next, fast.next, mid.next = fast, mid, temp
            fast = fast.next
            slow = slow.next.next

        return dummy.next
