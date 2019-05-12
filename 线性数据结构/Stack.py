# 只用 list 进行栈的实现, 不用链表实现了
class Stack(object):
    def __init__(self, maxLength=10):
        self.stack = [0]*maxLength
        self.maxLength = maxLength
        self.top = 0

    def clear(self):
        self.top = 0

    def push(self, e):
        assert self.top < self.maxLength
        self.stack[self.top] = e
        self.top += 1

    def pop(self):
        assert self.top > 0
        self.top -= 1
        return self.stack[self.top]

    def topValue(self):
        return self.stack[self.top-1]

    def isEmpty(self):
        return self.top == 0

def testStack():
    a = Stack()
    for i in range(10):
        a.push(i)
        print(a.topValue())
    print("pop:")
    for i in range(10):
        print(a.pop())

testStack()