# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for node in lists:
            while node:
                heapq.heappush(min_heap, node.val)
                node = node.next

        if not min_heap:
            return None

        head = ListNode(heapq.heappop(min_heap))
        curr_node = head

        while min_heap:
            curr_node.next = ListNode(heapq.heappop(min_heap))
            curr_node = curr_node.next

        return head
