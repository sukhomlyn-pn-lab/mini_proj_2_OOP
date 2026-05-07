# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def in_order(root: TreeNode):
            if root is None:
                return []
            values = []
            if root.left is None and root.right is None:
                values.append(root.val)
                return values
            values.extend(in_order(root.left))
            values.append(root.val)
            values.extend(in_order(root.right))
            return values
        values = in_order(root)
        first_val = values[0]
        for i in values[1:]:
            if i<=first_val:
                return False
            first_val = i
        return True
