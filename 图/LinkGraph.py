## PS: 其实这么做并不是很好... 既慢 又浪费空间... 其实为了方便去找下一个边 维护一个有序 Dict 是最好的方法 所以在这里只列出来接口, 暂时不进行实现
from 线性数据结构 import SingleLinkedList
class Edge(object):
    def __init__(self, v1, v2, val, next=None):
        self.v1 = v1
        self.v2 = v2
        self.val = val
        self.next = next

class EdgeList(SingleLinkedList):
    def __init__(self):
        SingleLinkedList.__init__()


class LinkGraph(object):
    def __init__(self, nodeNumber=10):
        self.nodeNumber = nodeNumber
        self.edgeList = [None]*nodeNumber
        self.edgeNumber = 0

    # 通过index获取firstEdge
    def firstEdgeByIndex(self, node):
        pass

    def nextEdgeByIndex(self, node, dst):
        pass

    def nextEdgeByEdge(self, edge):
        pass

    def isEdgeByIndex(self, v1, v2, val):
        pass

    def isEdgeByEdge(self, edge):
        pass

    def setEdgeByIndex(self, v1, v2, val):
        pass

    def setEdgeByEdge(self, edge):
        pass

    def setDoubleEdgeByIndex(self, v1, v2, val):
        pass

    def setDoubleEdgeByEdge(self, edge):
        pass

    def delEdgeByIndex(self, v1, v2):
        pass

    def delEdgeByEdge(self, edge):
        pass

    def getWeight(self, v1, v2):
        pass
