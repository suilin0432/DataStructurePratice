# 只用 list(循环队列, 因为不可能进行线性队列) 进行队列的实现, 不用链表实现了
class Queue(object):
    def __init__(self, maxLength=10):
        self.maxLength = maxLength
        self.queue = [-1]*(maxLength+1)
        self.head = 0
        self.tail = 0

    def clear(self):
        self.head = self.tail = 0

    def enqueue(self, e):
        assert (self.head+1)%(self.maxLength+1) != self.tail
        self.queue[self.head] = e
        self.head = (self.head+1)%(self.maxLength+1)

    def dequeue(self):
        assert self.head != self.tail
        t = (self.head-1)%(self.maxLength+1)
        self.head = t
        return self.queue[t]

    def isEmpty(self):
        return self.head == self.tail

    def isFull(self):
        return (self.head+1)%(self.maxLength+1) == self.tail

    def currentValue(self):
        return self.queue[(self.head-1)%(self.maxLength+1)]

    def length(self):
        if self.head == self.tail:
            return 0
        if (self.head+1)%(self.maxLength+1) == self.tail:
            return self.maxLength
        return (self.head + self.maxLength - self.tail)%(self.maxLength)
        # if self.head > self.tail:
        #     return self.head - self.tail
        # else:
        #     return

def testQueue():
    a = Queue()
    for i in range(10):
        a.enqueue(i)
        print(a.currentValue())
    print("dequeue:")
    for i in range(10):
        print(a.dequeue())
        print("length: ", a.length())
    print("test2:")
    a.enqueue(1000)
    for i in range(10):
        a.enqueue(i)
        print("length1: ", a.length())
        print(a.dequeue())
        print("length2: ", a.length())

testQueue()