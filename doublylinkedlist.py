class Node():
    def __init__(self, val) -> None:
        self.prev = None
        self.val = val
        self.next = None

class dll():
    def __init__(self) -> None:
        self.head = None
        self.tail = None


    def insertLast(self, val):
        newNode = Node(val)
        if(self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def insertFirst(self, val):
        newNode = Node(val)
        if(self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def deleteFirst(self):
        if(self.head == None):
            return -1
        elif(self.head == self.tail):
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def insertatn(self, val):
        pass