class SingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.curr = None
        self.length = 0
    def addNext(self, node):
        if not self.length:
            self.length += 1
            self.head = self.tail = self.curr = node
            return
        self.length += 1
        node.next = self.curr.next
        self.curr.next = node
        if self.tail == self.curr:
            self.tail = self.curr.next
    def append(self, node):
        if not self.length:
            self.length += 1
            self.head = self.tail = self.curr = node
            return
        self.length += 1
        self.tail.next = node
        self.tail = node

    def remove(self):
        assert self.length > 0
        assert self.curr != self.tail or self.length == 1
        self.length -= 1
        if self.length == 0:
            self.head = self.curr = self.tail = None
            return
        if self.curr.next == self.tail:
            t = self.tail
            self.tail = self.curr
            self.curr.next = None
            return t
        t = self.curr.next
        self.curr.next = self.curr.next.next
        return t

    def setFirst(self):
        assert self.length > 0
        self.curr = self.head

    def next(self):
        assert self.length > 0
        if self.curr.next:
            self.curr = self.curr.next

    def prev(self):
        assert self.length > 0
        assert self.head != self.curr
        node = self.head
        while node.next != self.curr:
            node = node.next
        self.curr = node

    def length(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def print(self):
        head = self.head
        while head:
            print(head.val, end="  ")
            head = head.next

    def printDetail(self):
        head = self.head
        index = 0
        while head and index < self.length:
            index += 1
            if head != self.head and head != self.tail:
                print("value:{0} next:{1}".format(head.val, head.next.val))
            else:
                print("value:{0} next:{1}".format(head.val, head.next))
            head = head.next

class SNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def testSingleLinkedList():
    a = SingleLinkedList()
    a.append(SNode(-1))
    for i in range(10):
        print("head: {0}  curr:{1}  tail:{2}, length:{3}".format(a.head.val, a.curr.val, a.tail.val, a.length))
        if i % 3 == 0:
            a.addNext(SNode(i))
        else:
            a.append(SNode(i))
            a.next()
    a.printDetail()

testSingleLinkedList()
