# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        queue = [root]
        values = [[root.val]]
        while queue:

            count = len(queue)
            floor = []
            for _ in range(count):
                value = queue.pop(0)
                if value.left:
                    floor.append(value.left.val)
                    queue.append(value.left)
                if value.right:
                    floor.append(value.right.val)
                    queue.append(value.right)
            values.append(floor)



        return values[:-1]
