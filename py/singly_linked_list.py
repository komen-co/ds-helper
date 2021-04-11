#Insert a singly linked list at the end of the list
import linked_list_node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    #Method to get the value of node at given index
    def getValueAt(self, index):
        current = self.head  
        count = 0

        while (current):
            if (count == index):
                print(current.val)
            count += 1
            current = current.next
        return 0
    #Method to insert node at the end
    def addAtEnd(self, val):
        newNode = Node(val)

        if self.head == None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode
    #Method to display the Singly Linked List
    def display(self):
        current = self.head

        if self.head == None:
            print("The Linked list is empty")
            return
        while current != None:
            print(current.val)
            current = current.next

    # A method to print the head node of the list
    def getHead(self):
        print(self.head.val)
