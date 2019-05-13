# 使用矩阵表示连通/距离的
class BasicGraph(object):
    def __init__(self, nodeNumber = 10):
        self.nodeNumber = nodeNumber
        self.MAXINT = 2**31-1
        self.matrix = [[self.MAXINT]*nodeNumber for _ in range(nodeNumber)]
        self.edgeNumber = 0
        # 标记是否访问过的
        self.mark = [0] * nodeNumber

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
        if self.matrix[src][dst] != self.MAXINT:
            self.edgeNumber += 1
        self.matrix[src][dst] = wt

    def delEdge(self, src, dst):
        assert src < self.nodeNumber and dst < self.nodeNumber
        if self.matrix[src][dst] != self.MAXINT:
            self.matrix[src][dst] = self.MAXINT
            self.edgeNumber -= 1

    def weight(self, src, dst):
        assert src < self.nodeNumber and dst < self.nodeNumber
        return self.matrix[src][dst]