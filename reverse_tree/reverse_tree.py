"""Reverse Tree"""

class TreeNode:
    def __init__(self, value, left:None, right:None):
        self.value = value
        self.left = left
        self.right = right


def invertTree(self, root: TreeNode) -> TreeNode:
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
