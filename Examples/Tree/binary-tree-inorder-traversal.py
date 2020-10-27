class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 



class Solution:
    
    def inorderTraversal(self, root: Node,result=[]) :
        if(root is not None):
            if(root.left is not None):
                self.inorderTraversal(root.left,result)
            result.append(root.val)
            if(root.right is not None ):
                self.inorderTraversal(root.right,result)
        return result   



# Driver code 
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 
# print "Preorder traversal of binary tree is"
# printPreorder(root) 
  

print(Solution().inorderTraversal(root)) 
  
# print "\nPostorder traversal of binary tree is"
# printPostorder(root) 