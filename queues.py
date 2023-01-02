class createnode:
    def __init__(self,value):
        self.value = value
        self.next = None
class queues:
    def __init__(self,value):
        newnode = createnode(value)
        self.first = newnode
        self.last = newnode
        self.length = 1
        
    def printqueue(self):
        if self.length == 0:
            return None
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
                
    def enqueue(self,value):
        newnode = createnode(value)
        if self.length == 0:
            self.first = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode
        self.length = self.length + 1
        
    def dequeue(self):
        if self.length == 0:
            return None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
            self.length = self.length - 1
            return temp