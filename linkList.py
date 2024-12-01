class sll:
    class node:
        def __init__(self,data):
            self.data = data
            self.next = None
    def __init__(self):
        self.head = None

    def insert (self,data):
        newnode = self.node(data)
        if self.head == None:
            self.head = newnode
            return
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = newnode

    def print(self):
        temp = self.head
        count = 0
        while (temp != None):
            print(temp.data)
            temp = temp.next
            count+= 1
        print("total size",count)
