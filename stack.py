class stack():
    def __init__(self, size):
        self.__a = []
        self.top = -1
        self.size = size

    def push(self, value):
        if(self.size <= self.top+1):
            return False
        else:
            self.__a.append(value)
            self.top += 1
            return self.top + 1

    def pop(self):
        if(self.top != -1):
            top -= 1
            return self.__a.pop()
    
    def top(self):
        return self.__a[self.top]

    def isempty(self):
        if(self.top == -1):
            return True
        return False