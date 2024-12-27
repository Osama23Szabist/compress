from linkList import dll
from bitarray import bitarray
from itertools import product

def char_convert_binary(word):
    binary = ''
    for data in word:
        hold = bin(ord(data))[2:]
        hold = hold.zfill(8)
        binary += hold
    return bitarray(binary)

def clean_a_name(name):
        find = name.find("(")
        while find != -1:
            name = name[0:find] + name[find+1:len(name)]
            find = name.find("(")

        find = name.find(")")
        while find != -1:
            name = name[0:find] + name[find+1:len(name)]
            find = name.find(")")

        find = name.find(",")
        while find != -1:
            name = name[0:find] + name[find+1:len(name)]
            find = name.find(",")

        find = name.find(" ")
        while find != -1:
            name = name[0:find] + name[find+1:len(name)]
            find = name.find(" ")

        return name

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
            self.inPreList = False
            self.replace = None
            
    def __init__(self):
        super().__init__()
        self.bitsaved = 0
        self.num = 1
        self.com = list(product([0, 1], repeat=self.num))
    
    def makeAtable(self):
        table = []
        temp = self.head
        while temp != None:
            if temp.worthit:
                data = char_convert_binary(temp.data)
                table.append((data,bitarray(temp.replace[1:])))
            temp = temp.next
        return table
        
    
    def insert (self,data,loc):
        if self.head == None:
            newnode = self.node(data,loc)
            self.head = self.tail= newnode
            return
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        newnode = self.node(data,loc,temp)
        temp.next = newnode
        self.tail = newnode

    def makeCombo(self):
        if len(self.com) == 0:
            self.num += 1
            self.com = list(product([0, 1], repeat=self.num))

    def comboList(self):
        if len(self.com) == 0:
            self.num += 1
            self.com = list(product([0, 1], repeat=self.num))
        hold = self.com[0]
        self.com.remove(self.com[0])
        hold = "1" + clean_a_name(str(hold))
        return hold

    
    def mod(self,nodeloc,loc):
        nodeloc.loc.append(loc)
        nodeloc.loc.sort(reverse = True)#we will make our own sort, future: we donot need loc
        nodeloc.count += 1
    
    def prelistCheck(self):
        temp = self.head
        while temp != None:
            temp.worthit = False#just in case

            if  not temp.inPreList:
                if len(self.com) == 0:
                    self.makeCombo()
                if (((len(self.com[0]))*temp.count) + (len(temp.data)*8)) < (temp.count*(len(temp.data)*8)):
                    temp.replace = self.comboList()
                    temp.worthit = True

            temp = temp.next
    
    def decrese(self):
        temp = self.head
        while temp != None:
            if not temp.worthit and not temp.inPreList:
                if temp == self.head:
                    self.head = temp.next
                    temp.pre = None
                else:
                    if temp.next == None:
                        self.tail = self.tail.pre
                        temp.pre.next = None
                    else:
                        temp.pre.next = temp.next
                        temp.next.pre = temp.pre
            temp = temp.next

    def print(self):
        temp = self.head
        count = 0
        while (temp != None):
            print("word:",temp.data,"count:",temp.count,"locs:",temp.loc,"wroth:",temp.worthit)
            temp = temp.next
            count+= 1
        print("total size",count,"bitsaved:",self.bitsaved)