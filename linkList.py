class sll():
    class node(): 
        def __init__(self,data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

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
        def inserttemp(self,head,anode):
            newnode = self.node(anode.data,anode.loc)
            newnode.count = anode.count
            newnode.worthit = anode.worthit
            if head == None:
                head = newnode
            else:
                temp = head
                while (temp.next != None):
                    temp = temp.next
                temp.next = newnode
        temp = self.head
        temp = temp.next
        newhead = None
        while temp != None:
            hold = temp
            minNode = hold
            while hold != None:
                if hold.loc[0] > minNode.loc[0]:
                    minNode = hold
                hold = hold.next
            if minNode != temp:
                inserttemp(newhead,minNode)
            else:
                inserttemp(newhead,temp) 
            inserttemp(newhead,minNode)
            temp = temp.next
        self.head = newhead

    def search(self,data):
        temp = self.head
        while(temp != None):
            if str(temp.data) == str(data):
                return True, temp
            temp = temp.next
        return False, None
    
   