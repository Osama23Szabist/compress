class sll:
    class node:
        def __init__(self,data,loc):
            self.count = 1
            self.data = data
            self.next = None
            self.loc= [loc]
            self.worthit = False
    def __init__(self):
        self.head = None
        self.bitsaved = 0

    def insert (self,data,loc):
        newnode = self.node(data,loc)
        if self.head == None:
            self.head = newnode
            return
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = newnode
    
    def mod(self,nodeloc,loc):
        nodeloc.loc.append(loc)
        nodeloc.count += 1
        ogsize = (len(nodeloc.data)*8)*nodeloc.count
        newsize = 0
        for data in nodeloc.loc:
            newsize += data.bit_length()
        newsize += (len(nodeloc.data)*8)
        if (ogsize)>(newsize):
            nodeloc.worthit = True
            self.bitsaved += ogsize-newsize

    def search(self,data):
        temp = self.head
        while(temp != None):
            if temp.data in data:
                return True, temp
            temp = temp.next
        return False, None
            

    def print(self):
        temp = self.head
        count = 0
        while (temp != None):
            print("word:",temp.data,"count:",temp.count,"locs:",temp.loc,"wroth:",temp.worthit)
            temp = temp.next
            count+= 1
        print("total size",count,"bitsaved:",self.bitsaved)
