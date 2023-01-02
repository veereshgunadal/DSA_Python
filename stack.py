class createnode:
    def __init__(self,value):
        self.value = value
        self.next = None
class stack:
    def __init__(self,value):
        newnode = createnode(value)
        self.top = newnode
        #print(self.top.value)
        self.length = 1
        
    def push(self,value):
        newnode = createnode(value)
        if self.top is None:
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode
        self.length = self.length + 1
        
    def printstack(self):
        if self.length == 0:
            return None
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            print("pop",temp.value)
            self.length = self.length - 1
            return temp
            
    