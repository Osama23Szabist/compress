class dll():
    class node(): 
        def __init__(self,data,pre = None):
            self.data = data
            self.next = None
            self.pre = pre

    def __init__(self):
        self.head = None
        self.tail = None
        
    def size(self):
        temp = self.head
        count = 0
        while temp != None:# count += 2 to improve the time
            count +=1
            temp = temp.next
        return count


    def insert (self,data):
        if self.head == None:
            newnode = self.node(data)
            self.head = self.tail= newnode
            return
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        newnode = self.node(data,temp)
        temp.next = newnode
        self.tail = newnode

    def sort(self):
        if not self.head or not self.head.next:
            return  # List is already sorted or empty
        
        self.head = self._merge_sort_rec(self.head)
    
    def _merge_sort_rec(self, head):
        if not head or not head.next:
            return head  # Base case: a single node or empty list is sorted

        # Step 1: Split the list into two halves
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        # Recursively sort both halves
        left = self._merge_sort_rec(head)
        right = self._merge_sort_rec(next_to_middle)

        # Step 2: Merge the sorted halves
        sorted_list = self._merge_sorted_lists(left, right)
        return sorted_list

    def _get_middle(self, head):
        # Use the slow and fast pointer approach to find the middle
        if not head:
            return head
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _merge_sorted_lists(self, left, right):
        if not left:
            return right
        if not right:
            return left

        # Choose the smaller value to continue merging
        if left.loc[0] <= right.loc[0]:
            result = left
            result.next = self._merge_sorted_lists(left.next, right)
        else:
            result = right
            result.next = self._merge_sorted_lists(left, right.next)

        return result

    # Utility functions for testing
    def append(self, data, loc):
        new_node = self.Node(data, loc)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def search(self,data):
        temp = self.head
        while(temp != None):
            if str(temp.data) == str(data):
                return True, temp
            temp = temp.next
        return False, None
    
   