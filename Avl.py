class tree:
    class node:
        def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None
            self.count = 1
            self.worthit = False
            self.inPreList = False
    
    def __init__(self,prelist):
        self.prelist = prelist
        self.root = None

    def insert(self,data):
        ans = self.search(data)
        if ans == None:
            temp = self.root
            newnode = self.node(data)
            while temp != None:
                if temp.data > data:
                    if temp.left == None:
                        temp.left = newnode

    def search(self,data):
        temp = self.root
        found = False
        while temp != None:
            if temp.data == data:
                found = True
                break
            else:
                if temp.data > data:
                    temp = temp.left 
                else:
                    temp = temp.right
        if found:
            return temp
        else:
            return None