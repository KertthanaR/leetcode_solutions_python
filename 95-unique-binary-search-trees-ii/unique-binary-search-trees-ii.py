# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        if n == 0:
            return []

        def build(lo, hi):
            if lo > hi:
                return [None]

            trees = []
            for root_val in range(lo, hi + 1):
                left_subtrees = build(lo, root_val - 1)
                right_subtrees = build(root_val + 1, hi)

                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        trees.append(root)

            return trees

        return build(1, n)