class sll():
    class node():
        
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

    def sort(self):#should have used dll :( should use megre sort 
        temp = self.head
        pre = self.head
        temp = temp.next
        while temp != None:
            hold = temp
            minNode = hold
            while hold != None:
                if hold.loc[0] > minNode.loc[0]:
                    minpre = pre
                    minNode = hold
                hold = hold.next
            if minNode != temp:
                temphold = pre.next
                pre.next = minNode
                tempmin = minpre.next
                minpre.next = temphold
            pre = temp
            temp = temp.next

    
    def mod(self,nodeloc,loc):
        nodeloc.loc.append(loc)
        nodeloc.loc.sort(reverse = True)#we will make our own sort
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
            if temp.data == data:
                return True, temp
            temp = temp.next
        return False, None
    
    def decrese(self):
        temp = self.head
        pre = self.head
        while temp != None:
            if not temp.worthit:
                if temp == self.head:
                    self.head = temp.next
                else:
                    pre.next = temp.next
            else:
                pre = temp
            temp = temp.next

    def removeData(self,text):
        temp = self.head
        less_size = 0
        while temp != None:
            less_size += temp.count
            text.remove(temp.data)
        return text,less_size

    def print(self):
        temp = self.head
        count = 0
        while (temp != None):
            print("word:",temp.data,"count:",temp.count,"locs:",temp.loc,"wroth:",temp.worthit)
            temp = temp.next
            count+= 1
        print("total size",count,"bitsaved:",self.bitsaved)
