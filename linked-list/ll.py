class Node:
    # Node structure 
    def __init__(self,data=None):
        self.data = data
        self.nextNode = None



class SingleLinkedList:
    # Initialize head of list
    def __init__(self):
        self.head = None

    # Print linked list
    def printLinkedList(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.nextNode
    
    def insertBeginning(self,newData):
        newNode = Node(newData)
        newNode.nextNode = self.head
        self.head = newNode
        return
    
    def insertAtEnd(self,newData):
        node = self.head
        while node is not None:
            if(node.nextNode is None):
                newNode = Node(newData)
                node.nextNode = newNode
                break
            node = node.nextNode
        return 
    
    def removeData(self,dataToBeRemoved):
        node = self.head
        prev = Node()
        while node is not None:
            if(node.data == dataToBeRemoved):
                prev.nextNode = node.nextNode
            prev = node
            node = node.nextNode
            



# Initialize list
head = SingleLinkedList()

# Initialize a data node
data1 = Node(1)
data2 = Node('Two')

# Linking
data1.nextNode = data2
data2.nextNode = Node(2)
head.head = data1

# Operations
head.insertBeginning('Im at beggining')
head.insertAtEnd('im at second last')
head.insertAtEnd('im at last')
head.removeData(2)


head.printLinkedList()