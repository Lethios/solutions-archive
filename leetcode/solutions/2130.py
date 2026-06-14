# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next

        sum_list = []
        sum_list.append(slow.val)

        while fast.next:
            slow = slow.next
            fast = fast.next.next

            sum_list.append(slow.val)

        n = len(sum_list) * 2

        i = len(sum_list)
        while slow.next:
            slow = slow.next
            sum_list[n - 1 - i] += slow.val

            i += 1

        return max(sum_list)
