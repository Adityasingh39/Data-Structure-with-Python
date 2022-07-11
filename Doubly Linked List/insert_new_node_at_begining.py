class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    # Create a Doubly Linked List
    def create_linked_list(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            newnode = Node(data)
            temp.next = newnode
            newnode.prev = temp
            self.last = newnode

    # Insert a New Node at begining
    def nodeBegining(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

    # forword direction
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end="---->")
            temp = temp.next

    # backword direction
    def display2(self):
        temp = self.last
        while temp is not None:
            print(temp.data,end="--->")
            temp = temp.prev


if __name__ == '__main__':
    obj = DoublyLinkedList()
    num = 0
    while num >= 0:
        num = int(input("\n Enter the number : "))
        if num < 0:
            break
        else:
            obj.create_linked_list(num)

    print("\n ************** Doubly Linked List ***************\n")
    obj.display()
    val = int(input("\n Enter the insert new Node at the begining : "))
    obj.nodeBegining(val)
    print("\n ************** Doubly Linked List ***************\n")
    obj.display()
    print("\n ************** Doubly Linked List in Reverse ***************\n")
    obj.display2()

# ----------------Written By : - Aditya Pratap Singh ------------------


