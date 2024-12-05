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

    def search(self,data):
        temp = self.head
        while(temp != None):
            if str(temp.data) == str(data):
                return True, temp
            temp = temp.next
        return False, None
    
   