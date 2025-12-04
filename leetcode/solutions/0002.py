# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        test = ListNode(0)
        current_node = test
        while l1 or l2 or carry > 0:
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0
            
            digit = num1 + num2 + carry
            carry = digit // 10
            digit = digit % 10

            current_node.next = ListNode(digit)
            current_node = current_node.next

        return test.next
