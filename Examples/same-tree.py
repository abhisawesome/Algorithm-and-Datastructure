# # Given two binary trees, write a function to check if they are the same or not.

# # Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Input:  
#            1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# Output: true
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if(p is None and q is None):
            return True
        if(p is None or q is None ):
            return False
        if(p.val != q.val):
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

one  = TreeNode(1)
oneLeft = TreeNode(2)
oneRight = TreeNode(3)

one.left = oneLeft
one.right = oneRight

two = TreeNode(1)
twoLeft = TreeNode(2)
twoRight = TreeNode(3)

two.left = twoLeft
two.right = twoRight

print(Solution().isSameTree(one,two))