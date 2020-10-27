# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSame(self,left:TreeNode,right:TreeNode)-> bool:
        if(left is None and right is None):
            return True
        if(left is None or right is None):
            return False
        if(left.val != right.val):
            return False
        return self.isSame(left.left,right.right) and self.isSame(left.right,right.left)
    def isSymmetric(self, root: TreeNode) -> bool:
        if(root is None):
            return False
        return self.isSame(root.left,root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(Solution().isSymmetric(root))