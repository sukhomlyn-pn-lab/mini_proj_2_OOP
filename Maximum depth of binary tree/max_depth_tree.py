"""Maximum depth of binary tree"""
class TreeNode:
    def __init__(self, value, left:None, right:None):
        self.value = value
        self.left = left
        self.right = right
def maxDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
