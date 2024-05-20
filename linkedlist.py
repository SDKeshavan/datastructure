class Node():
    def __init__(self, value) -> None:
        self.value = value 
        self.next = None       

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insertFirst(self, value):
        newNode = Node(value)
        if(self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertLast(self, value):
        newNode = Node(value)
        if(self.tail == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def insert(self, index, value):
        temp = self.head
        i = 0
        if(index == 0):
            self.insertFirst(value)
        else:
            while(i < index - 1 and temp.next):
                temp = temp.next
                i += 1
            if(not(temp.next)):
                self.insertLast(value)
            else:
                newNode = Node(value)
                newNode.next = temp.next
                temp.next = newNode

    def removeFirst(self):
        temp = self.head
        self.head = self.head.next
        del temp
    
    def removeLast(self):
        temp = self.head
        while(temp.next.next):
            temp = temp.next
        d = temp.next.next
        temp.next = None
        del d