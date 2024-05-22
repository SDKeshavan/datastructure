class BinarySearchTree:

    class node:
        def __init__(self):
            self.element = 0
            self.leftchild = None
            self.rightchild = None
            self.pos = -1
            self.parent = None


    def __init__(self):
        self.sz = 0
        self.root = None
        self.ht = 0
       
    def findElement(self,e,curnode):
        r = curnode
        while(r.element != e and (r.leftchild or r.rightchild)):
            if(r.element == e):
                break
            else:
                if(r.element < e):
                    r = r.rightchild
                else:
                    r = r.leftchild
        return r

    def insertElement(self,e):
        newNode = self.node()
        newNode.element = e
        if(not(self.root)):
            self.root = newNode
            self.root.pos = 1
            self.ht += 1
        else:
            temp = self.root
            while(temp.leftchild or temp.rightchild):
                if(temp.element < newNode.element and temp.rightchild):
                    temp = temp.rightchild
                elif(temp.element > newNode.element and temp.leftchild):
                    temp = temp.leftchild
                else:
                    break
            
            newNode.parent = temp
            if(temp.element < e):
                newNode.pos = (temp.pos * 2) + 1
                temp.rightchild = newNode
            else:
                newNode.pos = temp.pos * 2
                temp.leftchild = newNode


    def inorderTraverse(self,v):
        if(not v):
            return
        temp = v
        if(temp.leftchild):
            self.inorderTraverse(temp.leftchild)
        print(temp.element, end=" ")
        if(temp.rightchild):
            self.inorderTraverse(temp.rightchild)
            

    def minofsubtree(self, e):

        if(e.leftchild and e.rightchild):
            return min(self.minofsubtree(e.leftchild), self.minofsubtree(e.rightchild))
        elif(e.leftchild):
            return self.minofsubtree(e.leftchild)
        elif(e.rightchild):
            return self.minofsubtree(e.rightchild)
        else:
            return e.element

    def deleteElement(self,e):
        temp = self.findElement(e, self.root)
        if(temp.element != e):
            print("No such element")
            return -1
    
        if(self.isExternal(temp)):
            if(self.root == temp):
                self.root = None
                return
            if(temp.parent.element < temp.element):
                temp.parent.rightchild = None
            else:
                temp.parent.leftchild = None
        elif(temp.rightchild and temp.leftchild):
            ele = self.minofsubtree(temp.rightchild)
            eleNode = self.findElement(ele,self.root)
            print(eleNode.parent.element)
            temp.element = ele
            if(eleNode.parent.element < eleNode.element):
                eleNode.parent.rightchild = None
            else:
                eleNode.parent.leftchild = None
            
        else:
            if(temp.leftchild):
                child = temp.leftchid
            else:
                child = temp.rightchild

            if(temp == self.root):
                self.root = child
                return

            if(temp.parent.element < temp.element):
                temp.parent.rightchild = child
                temp.parent.rightchild.parent = temp.parent
            else:
                temp.parent.leftchild = child
                temp.parent.leftchild.parent = temp.parent

    def isExternal(self,curnode):
        if (curnode.leftchild == None and curnode.rightchild == None):
            return True
        else:
            return False

    def getChildren(self, ele):
        arr = []
        i = 0
        arr.append(ele)
        while(i < len(arr)):
            temp = arr[i]
            if(temp.leftchild):
                arr.append(temp.leftchild)
            elif(temp.rightchild):
                arr.append(temp.rightchild)
            i+=1
        return [i.element for i in arr]
    
    def preorderTraverse(self,v):
        temp = v
        print(temp.element, end=" ")
        if(temp.leftchild):
            self.preorderTraverse(temp.leftchild)
        if(temp.rightchild):
            self.preorderTraverse(temp.rightchild)
        
    def postorderTraverse(self,v):
        temp = v
        if(temp.leftchild):
            self.postorderTraverse(temp.leftchild)
        if(temp.rightchild):
            self.postorderTraverse(temp.rightchild)

        print(temp.element, end=" ")

    def findDepthIter(self,v):
        temp = v
        h = 0
        while(temp != self.root):
            h += 1
            temp = temp.parent
        
        return h

    
    def findDepth(self,ele):
        curnode = self.findElement(ele,self.root)
        if(curnode.element != ele):
            print("No such Element")
            return
        else:
            return self.findDepthIter(curnode)

    def findHeight(self,ele):

        temp = self.findElement(ele, self.root)
        
        if(temp.element == ele):
            if(temp.leftchild and temp.rightchild):
                max(self.findHeight(temp.leftchild)+1, self.findHeight(temp.rightchild)+1)
            elif(temp.leftchild):
                return self.findHeight(temp.leftchild)+1
            elif(temp.rightchid):
                return self.findHeight(temp.rightchild)+1
            else:
                return 1
        else:
            return "No such Element"
        
