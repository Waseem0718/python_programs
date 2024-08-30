class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
    

class LinkedList:
    def __init__(self):
        self.head =None

    def add_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref:
                n = n.ref
            n.ref = new_node

    def del_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.ref :
            slow = slow.ref
            fast = fast.ref.ref

        n = self.head
        while n.ref is not None:
            if n.ref.data == slow.data:
                break
            n = n.ref
        
        n.ref = slow.ref


    def print_ll(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,end="->")
                n = n.ref
            print("None")

ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
     
ll.del_middle()
ll.print_ll()