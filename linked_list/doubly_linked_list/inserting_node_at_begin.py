class Node:
    #creating a node
    def __init__(self,data):
        self.data = data
        self.pref = None
        self.nref = None
        
class DoublyLinkedList:
    #linking the nodes
    def __init__(self):
        self.head = None
    
    def insert_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def inserting_at_beginning(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            self.head.pref = new_node
            new_node.nref = self.head
            self.head = new_node
            new_node.pref = None

    #traverse in forward direction
    def print_ll_fd(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                 print(n.data,end="<->")
                 n = n.nref
            print("None") 
    #traverse in backward direction
    def print_ll_bd(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n.nref is not None:
                 n = n.nref
            while n is not None:
                 print(n.data,end="<->")
                 n = n.pref
            print("None") 
    
        
dll = DoublyLinkedList()
dll.insert_node(10)
dll.insert_node(20)
dll.insert_node(30)
dll.inserting_at_beginning(5)
dll.print_ll_fd()
