# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        array = []
        if root:
            queue = deque([root])
        else:
            return []

        level_size = 1
        while queue:
            subarray = []
            for i in range(level_size):
                node = queue.popleft()
                subarray.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            array.append(subarray)
            level_size = len(queue)

        return array
