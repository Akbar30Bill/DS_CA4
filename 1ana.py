class BST:
    def __init__(self, parrent, value):
        self.val = value
        self.parrent = parrent
        self.rightChild = None
        self.leftChild = None

    def insert(self, value):
        if (self is None):
            self = BST(value)
        else:
            if (self.val > value):
                if (self.leftChild == None):
                    self.leftChild = BST(self, value)
                    self.leftChild.parrent = self
                else:
                    self.leftChild.insert(value)
            else:
                if (self.rightChild == None):
                    self.rightChild = BST(self, value)
                    self.rightChild.parrent = self
                else:
                    self.rightChild.insert(value)

    def deleteNode(self):
        try:
            self.parrent.rightChild = None
            # if self.leftChild != None:
                # self.leftChild = self.parrent.rightChild
            self.parrent.rightChild = self.leftChild
            self.leftChild.parrent = self.parrent
        except:pass

    def findMax(self):
        if (self.rightChild == None):
            halfVal = int((self.val)/2)
            self.deleteNode()
            self.insert(halfVal)
            return self.val
        else:
            return self.rightChild.findMax()

N , T = list(map(int, input().split()))
arr = list(map(int, input().split()))
sum = 0
dummy = BST(None, None)
root = BST(dummy, arr[0])
for i in range (1, len(arr)):
    root.insert(arr[i])
for i in range(T):
    sum += root.findMax()
print(sum)
