class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 



class Traversal:
    def inOrderTraversal(self,root:Node,result=[])->[int]:
        if(root is not None):
            if(root.left is not None):
                self.inOrderTraversal(root.left,result)

            result.append(root.val)

            if(root.right is not None):
                self.inOrderTraversal(root.right,result)
        return result
    def preOrderTraversal(self,root:Node,result=[])->[int]:
        if(root is not None):
            result.append(root.val)
            if(root.left is not None):
                self.inOrderTraversal(root.left,result)
            if(root.right is not None):
                self.inOrderTraversal(root.right,result)
        return result

    def postOrderTraversal(self,root:Node,result=[])->[int]:
        if(root is not None):
            if(root.left is not None):
                self.inOrderTraversal(root.left,result)
            if(root.right is not None):
                self.inOrderTraversal(root.right,result)
            result.append(root.val)
        return result

root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 

print("in order traversal",Traversal().inOrderTraversal(root))
print("pre order traversal",Traversal().preOrderTraversal(root))
print("post order traversal",Traversal().postOrderTraversal(root))