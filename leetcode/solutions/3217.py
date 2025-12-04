# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev, current = dummy, head

        delete = set(nums)

        while current:
            if current.val in delete:
                prev.next, current = current.next, current.next
            else:
                prev.next = current
                prev, current = current, current.next

        return dummy.next
