from linkList import dll
class word(dll):
    class node(dll.node):
        def __init__(self,data,loc,pre = None):
            super().__init__(data,pre)
            if type(loc) == list:
                self.loc = loc
            else:
                self.loc= [loc]
            self.count = 1
            self.worthit = False
    def __init__(self):
        super().__init__()
        self.bitsaved = 0

    
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