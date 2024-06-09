class AVLTree:
    class Node:
        def __init__(self, element, left =None, right=None):
            self.element = element
            self.leftchild = left
            self.rightchild = right
            self.parent = None

    def __init__(self):
        self.root = None

    def getHeight(self, node):
        if not(node):
            return 0
        return max(self.getHeight(node.leftchild), self.getHeight(node.rightchild))+1

    def getBalance(self, node):
        if not(node):
            return 0
        return self.getHeight(node.leftchild) - self.getHeight(node.rightchild)

    def rightRotate(self, node):
        print("Rotating Right")
        if node is None or node.leftchild is None:
            return
        z = node.leftchild
        t = z.rightchild

        node.leftchild = t
        z.rightchild = node
        
        z.parent = node.parent

        if(not node.parent):
            self.root = z
        elif(node is node.parent.rightchild):
            node.parent.rightchild = z
        elif(node is node.parent.leftchild):
            node.parent.leftchild = z

        node.parent = z
        if(t):
            t.parent = node

            


    def leftRotate(self, node):
        print("Rotating left")
        if node is None or node.rightchild is None:
            return
        z = node.rightchild
        t = z.leftchild

        node.rightchild = t
        z.leftchild = node

        z.parent = node.parent

        if(not node.parent):
            self.root = z
        elif(node is node.parent.rightchild):
            node.parent.rightchild = z
        elif(node is node.parent.leftchild):
            node.parent.leftchild = z
        node.parent = z
        if(t):
            t.parent = node

    def insert(self, node, element):
        if(not(node)):
            self.root = element
            return
        temp = self.root
        while(temp.rightchild or temp.leftchild):
            if(temp.rightchild and temp.element <= element.element):
                temp = temp.rightchild
            elif(temp.leftchild and temp.element > element.element):
                temp = temp.leftchild
            else:
                break
        
        if(temp.element <= element.element):
            temp.rightchild = element
        else:
            temp.leftchild = element
        element.parent = temp   
        self.checkBalance(element.parent)

    def findNode(self, element):
        temp = self.root
        
        while(temp):
            if(temp.element == element):
                return temp

            if(temp.element < element):
                temp = temp.rightchild
            else:
                temp = temp.leftchild
        
        return -1


    def deleteNode(self, element, node):
        if not node:
            return node
        
        if element < node.element:
            self.deleteNode(element, node.leftchild)
        elif element > node.element:
            self.deleteNode(element, node.rightchild)
        else:

            if not node.leftchild:
                temp = node.rightchild
                if(node == self.root):
                    self.root = temp
                    return
                if(node is node.parent.rightchild):
                    node.parent.rightchild = temp
                else:  
                    node.parent.leftchild = temp
                node = None
                return temp
            elif not node.rightchild:
                temp = node.leftchild
                if(node == self.root):
                    self.root = temp
                    return
                if(node is node.parent.rightchild):
                    node.parent.rightchild = temp
                else:  
                    node.parent.leftchild = temp
                node = None
                return temp
            

            temp = self.getMinValueNode(node.rightchild)

            node.element = temp.element

            self.deleteNode(temp.element, node.rightchild)

        if node is None:
            return node

        if node.leftchild:
            node.leftchild.parent = node
        if node.rightchild:
            node.rightchild.parent = node

        self.checkBalance(node)
        return node
    
    def getMinValueNode(self, node):
        current = node
        while current.leftchild is not None:
            current = current.leftchild
        return current
                

    def checkBalance(self, node):
        if(not node.parent or not node):
            return
        temp = node
        print("Chck bl ",temp.element)
        print("Entering Chck Bal")
        while(temp):
            bf = self.getBalance(temp)
            print(temp.element)
            if(bf > 1 and self.getBalance(temp.leftchild) >= 0):
                self.rightRotate(temp)
            elif(bf > 1 and self.getBalance(temp.leftchild) < 0):
                self.leftRotate(temp.leftchild)
                self.rightRotate(temp)
            elif(bf<-1 and self.getBalance(temp.rightchild) > 0):
                self.rightRotate(temp.rightchild)
                self.leftRotate(temp)
            elif(bf<-1 and self.getBalance(temp.rightchild) <=0):
                self.leftRotate(temp)
            temp = temp.parent


    def inOrder(self, root):
        if(not root):
            return
        if(root.leftchild):
            self.inOrder(root.leftchild)
        print(root.element, end=" ")
        if(root.rightchild):
            self.inOrder(root.rightchild)


    def insertElement(self, element):
        newNode = self.Node(element)
        self.insert(self.root, newNode)
        

    def printTree(self, node=None):
        if node is None:
            node = self.root
        
        if(node is None):
            print("MTY")
            return

        if node.leftchild:
            self.printTree(node.leftchild)
        if node.rightchild:
            self.printTree(node.rightchild)

        print("Node:", node.element, "=>", end=" ")
        if node.leftchild:
            print(node.leftchild.element, end=" ")
        else:
            print("-", end=" ")
        if node.rightchild:
            print(node.rightchild.element, end=" ")
        else:
            print("-", end=" ")

        print("\n---------------------------")

# Driver code to demonstrate the usage of AVLTree
if __name__ == "__main__":
    avl = AVLTree()
    elements = [33, 13, 52, 9, 21, 61, 8, 11]
    # elements = [1, 2, 3]
    for element in elements:
        avl.insertElement(element)
    
    avl.printTree()

    avl.deleteNode(13, avl.root)
    avl.deleteNode(9, avl.root)
    # avl.deleteNode(33, avl.root)
    # avl.deleteNode(61, avl.root)
    # avl.deleteNode(11, avl.root)
    # avl.deleteNode(8, avl.root)
    # avl.deleteNode(52, avl.root)
    # avl.deleteNode(21, avl.root)

    print("Inorder traversal of the constructed AVL tree is")
    avl.inOrder(avl.root)
    print()
    avl.printTree()
