# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []

        if not root:
            return res

        def traverse(node: TreeNode):
            if node.left:
                traverse(node.left)

            res.append(node.val)

            if node.right:
                traverse(node.right)

        traverse(root)

        return res
