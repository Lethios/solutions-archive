# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_A, node_B = headA, headB
        while node_A != node_B:
            node_A = node_A.next if node_A else headB
            node_B = node_B.next if node_B else headA
        
        return node_A
