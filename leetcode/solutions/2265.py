# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def avg_check(total_sum: int, count: int, node_val: int) -> bool:
    if total_sum // count == node_val:
        return True

    return False


class Solution:
    def traverse(self, node: TreeNode):
        if node is None:
            return (0, 0, 0)

        if node.left or node.right:
            l_sum, l_count, l_res = self.traverse(node.left)
            r_sum, r_count, r_res = self.traverse(node.right)

            total_sum = l_sum + r_sum + node.val
            total_count = l_count + r_count + 1

            res = 1 if avg_check(total_sum, total_count, node.val) else 0
            total_res = l_res + r_res + res

            return (total_sum, total_count, total_res)

        return (node.val, 1, 1)

    def averageOfSubtree(self, root: TreeNode) -> int:
        _, _, res = self.traverse(root)

        return res
