# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root.left, root.right)])

        while queue:
            node_l, node_r = queue.popleft()

            if not node_l and not node_r:
                continue
            if not node_l or not node_r:
                return False
            if node_l.val != node_r.val:
                return False

            queue.append((node_l.left, node_r.right))
            queue.append((node_l.right, node_r.left))

        return True
