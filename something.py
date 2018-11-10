class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key

    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            if data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    def search(self,key):
        if self.data==key or self.data is None:
            return self.data
        else:
            if key>self.data:
                return self.right.search(key)
            if key<self.data:
                return self.left.search(key)
            

    def printInorder(self):
        if self.left:
            self.left.printInorder()
        if self.data is not None:
            print(self.data,end=" ")
        if self.right:
            self.right.printInorder()

    def printPreorder(self):
        print(self.data,end=" ")
        if self.left:
            self.left.printPreorder()
        if self.right:
            self.right.printPreorder()


    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.data,end=" ")
    def minValueNode(self): 
        if self.left:
            curr=self.left
    # loop down to find the leftmost leaf 
            while(curr is not None): 
                curr = curr.left

            return curr
        else:
            return self.data
    
    def deleteNode(self,key):
        if self.data==None:
            return None
        elif self.data>key:
            return self.left.deleteNode(key)
        elif self.data<key:
            return self.right.deleteNode(key)
        else:
            if self.left==None and self.right==None:
                self.data=None
            elif self.left==None:
                temp=self.right
                self.data=None
                return temp
            elif self.right==None:
                temp=self.left
                self.data=None
                return temp
                
            else:
                temp=self.right.minValueNode()
                self.data=temp
                self.right.deleteNode(temp)
root=Node(10)
print(root.data)
root.insert(11)
root.insert(12)
root.insert(15)
root.insert(8)
root.insert(9)
root.insert(7)
print("Inorder Traversal")
root.printInorder()
print()
print("Postorder Traversal")
root.postOrder()
print()
print("Preorder Traversal")
root.printPreorder()
print()
root.deleteNode(10)
root.printInorder()
print()
print(root.data)

                
