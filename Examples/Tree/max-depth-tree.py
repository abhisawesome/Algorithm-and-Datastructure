#  Given a binary tree, find its maximum depth.

#  The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output 3

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def maxDepth(root:TreeNode)->int:
    if(root is None): 
        return 0
    else:
        lDepth = maxDepth(root.left)
        rDepth = maxDepth(root.right)
        
        return max(lDepth,rDepth) + 1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)

print(maxDepth(root))

