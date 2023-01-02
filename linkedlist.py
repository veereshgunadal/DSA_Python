class createnode:
    def __init__(self,value):
        self.value = value
        self.next = None

class linkedlist:
    def __init__(self,value):
        newnode = createnode(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1
        
    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self,value):
        newnode = createnode(value)
        if self.head is not None:
            self.tail.next = newnode
            self.tail = newnode
        else:
            self.head = newnode
            self.tail = newnode
        self.length += 1
        
    def pop(self):
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
            self.tail = pre
        self.tail.next = None
        self.length -= 1
        print("pop value",temp.value)
        return temp
    
    def prepend(self,value):
        newnode = createnode(value)
        if self.head is not None:
            newnode.next = self.head
            self.head = newnode
        self.length += 1
        
    def popfirst(self):
        temp = self.head
        self.head = self.head.next 
        temp.next = None
        print("pop",temp.value)
        self.length -= 1
        return temp
    
    def get(self,index):
        temp = self.head
        for i in range(index):
            temp = temp.next
        print("value",temp.value)
        return temp
    
    def setvalue(self,index,value):
        temp = self.get(index)
        temp.value = value
        
    def remove(self,index):
        pre = self.get(index-1)
        temp = self.get(index)
        pre.next = temp.next
        temp.next = None        
        return temp
            
    def reverse(self):
        temp = self.tail
        temp1 = temp
        #print(temp.value)
        for i in range(self.length):
            node = self.pop()
            #print(node, node.value)
            temp.next = node
            temp = temp.next
            #print(temp.value)
        self.head = temp1
        self.tail = temp
            
            
            
            
            
            
            
            