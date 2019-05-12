import random
# 这里采用 最大堆
class PriorityQueue(object):
    def __init__(self, maxLength=20):
        self.maxLength = maxLength
        self.heap = [-1]*maxLength
        self.length = 0

    def heapSize(self):
        return self.length

    def isLeaf(self, node):
        return node >= self.maxLength // 2 and node < self.maxLength

    def leftChild(self, node):
        assert node * 2 + 1 < self.maxLength
        return node * 2 + 1

    def rightChild(self, node):
        assert node * 2 + 2 < self.maxLength
        return node * 2 + 2

    def parent(self, node):
        assert node < self.maxLength and node > 0
        return (node - 1) // 2

    def getLeftChild(self, node):
        assert node * 2 + 1 < self.maxLength
        return self.heap[node * 2 + 1]

    def getRightChild(self, node):
        assert node * 2 + 2 < self.maxLength
        return self.heap[node * 2 + 2]

    def getParent(self, node):
        assert node < self.maxLength
        return self.heap[(node - 1) // 2]

    # 插入新的元素
    def insert(self, val):
        assert self.length < self.maxLength
        if self.length == 0:
            self.heap[0] = val
            self.length = 1
            return
        self.heap[self.length] = val
        node = self.length
        self.length += 1
        p = self.parent(node)
        while self.heap[node] > self.heap[p]:
            t = self.heap[p]
            self.heap[p] = self.heap[node]
            self.heap[node] = t
            if p > 0:
                node = p
                p = self.parent(node)

    # 将最大的元素取出 然后重新维护
    def pop(self):
        pass

    # 将指定位置的元素取出 然后维护堆
    def remove(self, pos):
        pass

    def print(self):
        print(self.heap)

def testPriorityQueue():
    H = PriorityQueue()
    l = [i for i in range(1, 21)]
    random.shuffle(l)
    for i in l:
        H.insert(i)
    H.print()

testPriorityQueue()