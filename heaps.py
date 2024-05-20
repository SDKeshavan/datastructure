class BinHeap():
    def __init__(self):
        self.heapList = []
        self.currentSize = 0

    def upHeapp(self,i):
        while i > 0 and self.heapList[i] < self.heapList[i-1 // 2]:
            self.heapList[i], self.heapList[i-1 // 2] = self.heapList[i-1 // 2], self.heapList[i]
            i = i-1 // 2
     
            
    def insert(self,k):
        curInd = len(self.heapList)
        self.heapList.append(k)
        if(curInd > 0):
            pnode = int((curInd-1)/2)
            while(self.heapList[pnode] > self.heapList[curInd]):
                temp = self.heapList[pnode]
                self.heapList[pnode] = self.heapList[curInd]
                self.heapList[curInd] = temp
                curInd = pnode
                pnode = int((curInd-1)/2)
        self.currentSize += 1


    def downHeap(self,i):
        while i*2+1 < len(self.heapList) and i*2+2 < len(self.heapList):
            lc = i*2+1
            rc = i*2+2
            if(self.heapList[i]>self.heapList[lc] and self.heapList[i]>self.heapList[rc]):
                if(self.heapList[lc]<self.heapList[rc]):
                    self.heapList[lc], self.heapList[i] = self.heapList[i], self.heapList[lc]
                    i = lc
                else:
                    self.heapList[rc], self.heapList[i] = self.heapList[i], self.heapList[rc]
                    i = rc

            else:
                if(self.heapList[lc] < self.heapList[i]):
                    self.heapList[lc], self.heapList[i] = self.heapList[i], self.heapList[lc]
                    i = lc
                elif(self.heapList[rc] < self.heapList[i]):
                    self.heapList[rc], self.heapList[i] = self.heapList[i], self.heapList[rc]
                    i = rc
                else:
                    break

    def minChild(self,i):
        pass

    def deleteop(self):
        self.heapList[0] = self.heapList[-1]
        del self.heapList[-1]
        self.downHeap(0)
        self.printHeap()
    
    def buildHeap(self,alist,k):

        for ele in alist:
            self.insert(ele)

        self.printHeap()



    def printHeap(self):
        print(self.heapList)
        


def main():
    heap = BinHeap()
    arraysize=int(input())
    arr = list(map(int, input().split()))
    k=int(input())
    heap.buildHeap(arr,k)
    inputs = int(input())
    while inputs > 0:
        command = input()
        operation = command.split()
        if (operation[0] == "I"):
            heap.insert(int(operation[1]))
            heap.printHeap()
        elif (operation[0] == "D"):
            heap.deleteop()
            
        elif (operation[0] == "K"):
            kthlargest=heap.klargest(arr,k)
            print(kthlargest)
        

              
        inputs -= 1

if __name__ == '__main__':
    main()