class tree:
    class node:
        def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None
            self.pre = None
            self.count = 1
            self.worthit = False
            self.inPreList = False
    
    def __init__(self,prelist):
        self.prelist = prelist
        self.root = None

    def balance(self,thenode,rh,lh):
        if (rh-lh) > 1:
            pass 
        elif (rh-lh) < -1:
            pass


    def heights(self,thenode,h = 0):
        if thenode.right != None and thenode.left != None:
            h += 1
            h = self.heights(thenode.right,h)
            h = self.heights(thenode.left,h)
        else:
            if thenode.right != None:
                h += 1
                h = self.heights(thenode.right,h)
            elif thenode.left != None:
                h += 1
                h = self.heights(thenode.left,h)
        return h

    def insert(self,data):
        ans = self.search(data)
        if ans == None:
            temp = self.root
            newnode = self.node(data)
            while temp != None:
                if temp.data > data:
                    if temp.left == None:
                        newnode.pre = temp
                        temp.left = newnode
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right == None:
                        newnode.pre = temp
                        temp.right = newnode
                        break
                    else:
                        temp = temp.right
            while temp != self.root:
                self.balance(temp,self.heights(temp.right),self.heights(temp.right))
                temp = temp.pre

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