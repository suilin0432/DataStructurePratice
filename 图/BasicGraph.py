import collections
# 使用矩阵表示连通/距离的
class BasicGraph(object):
    def __init__(self, nodeNumber = 10):
        self.nodeNumber = nodeNumber
        self.MAXINT = 2**31-1
        self.matrix = [[self.MAXINT]*nodeNumber for _ in range(nodeNumber)]
        self.edgeNumber = 0
        # 标记是否访问过的
        self.mark = [False] * nodeNumber

    # 会默认将所有的0->MAXINT
    def edges(self, matrix):
        self.matrix = matrix
        for i in range(self.nodeNumber):
            for j in range(self.nodeNumber):
                if self.matrix[i][j] == 0:
                    self.matrix[i][j] = self.MAXINT

    def firstEdge(self, node):
        assert node < self.nodeNumber
        for i in range(self.nodeNumber):
            if self.matrix[node][i] != self.MAXINT:
                return (node, i)
        return None

    def nextEdge(self, node, dst):
        assert node < self.nodeNumber and dst < self.nodeNumber
        for i in range(dst+1, self.nodeNumber):
            if self.matrix[node][i] != self.MAXINT:
                return (node, i)
        return None

    def isEdge(self, node, dst):
        assert node < self.nodeNumber and dst < self.nodeNumber
        return self.matrix[node][dst] != self.matrix

    # 假设每两个节点之间只能有一条边
    def setEdge(self, src, dst, wt):
        assert wt < self.MAXINT
        assert src < self.nodeNumber and dst < self.nodeNumber
        if self.matrix[src][dst] == self.MAXINT:
            self.edgeNumber += 1
        self.matrix[src][dst] = wt

    def setDoubleEdge(self, src, dst, wt):
        assert wt < self.MAXINT
        assert src < self.nodeNumber and dst < self.nodeNumber
        if self.matrix[src][dst] == self.MAXINT:
            self.edgeNumber += 1
        self.matrix[src][dst] = wt
        if self.matrix[dst][src] == self.MAXINT:
            self.edgeNumber += 1
        self.matrix[dst][src] = wt

    def delEdge(self, src, dst):
        assert src < self.nodeNumber and dst < self.nodeNumber
        if self.matrix[src][dst] != self.MAXINT:
            self.matrix[src][dst] = self.MAXINT
            self.edgeNumber -= 1

    def weight(self, src, dst):
        assert src < self.nodeNumber and dst < self.nodeNumber
        return self.matrix[src][dst]

    def markReset(self):
        self.mark = [False] * self.nodeNumber

    # 进行图的一些扩展功能实现
    def preDfsTravel(self, begin=0):
        self.markReset()
        self.dfsTravel(begin, True)
    def postDfsTravel(self, begin=0):
        self.markReset()
        self.dfsTravel(begin, False)
    def dfsTravel(self, begin=0, pre=True):
        # pre表示是否进行前序周游
        # begin表示开始的节点
        # print(begin)
        self.mark[begin] = True
        if pre:
            print(begin, end=" ")
        next = self.firstEdge(begin)
        while next:
            v1, v2 = next
            if not self.mark[v2]:
                self.dfsTravel(v2, pre)
            next = self.nextEdge(v1, v2)
        if not pre:
            print(begin, end=" ")

    def bfsTravel(self, begin=0):
        self.markReset()
        queue = collections.deque()
        queue.append(begin)
        self.mark[begin] = True
        while queue:
            node = queue.popleft()
            print(node, end=" ")
            next = self.firstEdge(node)
            while next:
                v1, v2 = next
                if not self.mark[v2]:
                    queue.append(v2)
                    self.mark[v2] = True
                next = self.nextEdge(v1, v2)

    def topSort(self):
        self.markReset()
        for i in range(0, self.nodeNumber):
            if not self.mark[i]:
                self.dfsTravel(i, False)



def testBasicGraph1():
    graph = BasicGraph(8)
    adjMatrix = [
        [0, 2, 8, 1, 0, 0, 0, 0],
        [2, 0, 6, 0, 1, 0, 0, 0],
        [8, 6, 0, 7, 4, 2, 2, 0],
        [1, 7, 0, 0, 0, 0, 9, 0],
        [0, 1, 4, 0, 0, 3, 0, 9],
        [0, 2, 0, 0, 3, 0, 4, 6],
        [0, 0, 2, 9, 0, 4, 0, 2],
        [0, 0, 0, 0, 9, 6, 2, 0]
    ]
    l = [(0, 1, 2), (0, 2, 8), (0, 3, 1), (1, 2, 6), (1, 4, 1), (2, 3, 7), (2, 4, 4), (2, 5, 2), (2, 6, 2), (3, 6, 9),
         (4, 5, 3), (4, 7, 9), (5, 6, 4), (5, 7, 6), (6, 7, 2)]
    for i in l:
        graph.setDoubleEdge(i[0], i[1], i[2])
        print(graph.edgeNumber)
    for i in graph.matrix:
        for j in i:
            if j == graph.MAXINT:
                print(0, end=", ")
            else:
                print(j, end=", ")
        print()
    print(graph.nextEdge(0, 2))
    graph.preDfsTravel()
    print()
    graph.postDfsTravel()
    print()
    graph.bfsTravel()

def testBasicGraph2():
    graph = BasicGraph(7)
    matrix = [
        [0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0]
    ]
    graph.edges(matrix)
    graph.topSort()
    print()
    graph.preDfsTravel()
    print()

# testBasicGraph1()
testBasicGraph2()