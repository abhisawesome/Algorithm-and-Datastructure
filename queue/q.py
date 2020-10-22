class Queue:
    def __init__(self,queue):
        self.queue = queue
    
    # Enqueue Operation
    def enqueue(self,value):
        self.queue.append(value)

    # Dequeue Operation
    def dequeue(self):
        self.queue = self.queue[1:]
    
    def returnQueue(self):
        return self.queue

q = Queue([])
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print('After enqueue',q.returnQueue())
q.dequeue()
print('After dequeue',q.returnQueue())