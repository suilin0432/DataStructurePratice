import collections
# 使用数组
class BinaryTree(object):
    def __init__(self, maxLength=15):
        self.maxLength = maxLength
        self.tree = [-1] * maxLength

    def getLeft(self, node):
        assert node * 2 + 1 < self.maxLength
        return self.tree[node * 2 + 1]

    def getRight(self, node):
        assert node * 2 + 2 < self.maxLength
        return self.tree[node * 2 + 2]

    def setLeft(self, node, value):
        assert node * 2 + 1 < self.maxLength
        self.tree[node * 2 + 1] = value

    def setRight(self, node, value):
        assert node * 2 + 2 < self.maxLength
        self.tree[node * 2 + 2] = value

    def isLeaf(self, node):
        return node >= self.maxLength // 2 and node < self.maxLength

    def isLegal(self, node):
        return node < self.maxLength

    def preTravel(self, root):
        print(self.tree[root])
        if self.isLegal(root*2+1):
            self.preTravel(root*2+1)
        if self.isLegal(root*2+2):
            self.preTravel(root*2+2)

    def queueTravel(self):
        queue = collections.deque()
        queue.append(0)
        while queue:
            node = queue.popleft()
            print(self.tree[node])
            if self.isLegal(node * 2 + 1):
                queue.append(node * 2 + 1)
            if self.isLegal(node * 2 + 2):
                queue.append(node * 2 + 2)




def testBinaryTree():
    T = BinaryTree()
    T.tree[0] = 1
    queue = collections.deque()
    queue.append(0)
    num = 2
    while queue:
        node = queue.popleft()
        if T.isLegal(node * 2 + 1):
            T.setLeft(node, num)
            num+=1
            queue.append(node * 2 + 1)
        if T.isLegal(node * 2 + 2):
            T.setRight(node, num)
            num += 1
            queue.append(node * 2 + 2)
    T.queueTravel()

testBinaryTree()
