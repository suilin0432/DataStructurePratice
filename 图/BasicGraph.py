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
        assert node <
        for i in range(self.nodeNumber):
            if self.matrix[node][i] != self.MAXINT:
                return (node, i)
        return None

    def nextEdge(self, node, dst):
        for i in range(dst+1, self.nodeNumber):
            if self.matrix[node][i] != self.MAXINT:
                return (node, i)
        return None

    def isEdge(self, node, dst):
