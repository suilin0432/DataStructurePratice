import random
import time
# 这里采用 最大堆

class PriorityQueue(object):
    def __init__(self, maxLength=20):
        self.maxLength = maxLength
        self.heap = [-1]*maxLength
        self.length = 0

    def buildHeap(self, l):
        self.heap = l
        self.length = len(l)
        for i in reversed(range((self.length-1)//2)):
            self.siftDown(i)

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

    def hasRight(self, node):
        return node * 2 + 2 < self.length

    def hasLeft(self, node):
        return node * 2 + 1 < self.length

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
        assert self.length > 0
        self.length -= 1
        element = self.heap[0]
        self.heap[0] = self.heap[self.length]
        node = 0
        self.siftDown(node)
        return element

    def siftDown(self, node):
        while self.hasLeft(node):
            # if self.length == 5:
            #     print("## node={0} left={1} right={2}".format(node, 2*node+1, 2*node+2), end=" ")
            #     self.print()
            left = self.leftChild(node)
            right = self.rightChild(node) if self.hasRight(node) else -1
            leftValue = self.getLeftChild(node)
            rightValue = self.getRightChild(node) if self.hasRight(node) else -1
            maxValue = 0
            maxIndex = 0
            if leftValue >= rightValue:
                maxValue = leftValue
                maxIndex = left
            else:
                maxValue = rightValue
                maxIndex = right
            # 交换
            if maxValue > self.heap[node]:
                t = self.heap[node]
                self.heap[node] = self.heap[maxIndex]
                self.heap[maxIndex] = t
                node = maxIndex
            else:
                break
    # 将指定位置的元素取出 然后维护堆
    def remove(self, node):
        assert node < self.length
        self.length -= 1
        element = self.heap[node]
        self.heap[node] = self.heap[self.length]
        self.siftDown(node)
        return element

    def print(self):
        print(self.heap)

def testPriorityQueue1():
    t1 = time.time()
    n = 10000000
    H = PriorityQueue(n)
    l = [i for i in range(1, n+1)]
    random.shuffle(l)
    # print(l)
    for i in l:
        H.insert(i)
    # H.print()
    print("buildTime:", time.time() - t1)
    return
    index = n
    # l = []
    while H.length:
        k = H.pop()
        assert k == index
        # l.append(k)
        index -= 1
        # print(k, end=" ")
        # print(H.length, end=" ")
        # H.print()
    # print()
    # print(l)
    t2 = time.time()
    print("time: ",t2 - t1)

def testPriorityQueue2():
    n = 10000
    H = PriorityQueue(n)
    l = [i for i in range(1, n+1)]
    random.shuffle(l)
    for i in l:
        H.insert(i)
    H.print()
    for i in range(n-1, -1, -1):
        h = H.heap[i]
        e = H.remove(i)
        assert h == e

def testPriorityQueue3():
    t1 = time.time()
    n = 10000000
    H = PriorityQueue(n)
    l = [i for i in range(1, n+1)]
    random.shuffle(l)
    H.buildHeap(l)
    print("buildTime:", time.time()-t1)
    return
    # H.print()
    index = n
    while H.length:
        k = H.pop()
        assert k == index
        l.append(k)
        index -= 1
    t2 = time.time()
    print(t2-t1)

# testPriorityQueue1()
# testPriorityQueue2()
testPriorityQueue3()
testPriorityQueue1()