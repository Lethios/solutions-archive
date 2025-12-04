# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        current_node = head

        while list1 and list2:
            num1 = list1.val
            num2 = list2.val

            if num1 < num2:
                current_node.next = ListNode(num1)
                current_node = current_node.next
                list1 = list1.next

            elif num2 < num1:
                current_node.next = ListNode(num2)
                current_node = current_node.next
                list2 = list2.next

            else:
                current_node.next = ListNode(num1)
                current_node = current_node.next
                list1 = list1.next
                
                current_node.next = ListNode(num2)
                current_node = current_node.next
                list2 = list2.next
        
        if list1:
            current_node.next = list1
        if list2:
            current_node.next = list2

        return head.next
