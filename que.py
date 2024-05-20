class que:
    def __init__(self, size):
        self.__a = []
        self.front = -1
        self.rear = 0
        self.size = size
        for i in range(self.size):
            self.__a.append(None)


    def push(self, value):
        self.__a[self.rear] = value
        self.rear = (self.rear + 1) % self.size

    def pop(self):
        self.__a[self.front] = None
        self.front = (self.front + 1) % self.size

    def size(self):
        if(self.front<self.rear):
            return self.rear + 1 - self.front
        else:
            pass

    def isempty(self):
        if self.size() == 0:
            return True
        return False

    