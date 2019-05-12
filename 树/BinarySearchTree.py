import collections
class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def clear(self):
        self.root = None

    def insert(self, node):
        if not self.root:
            self.root = node
            return
        root = self.root
        while True:
            if node.val >= root.val:
                if root.right == None:
                    root.right = node
                    break
                else:
                    root = root.right
            elif node.val < root.val:
                if root.left == None:
                    root.left = node
                    break
                else:
                    root = root.left

    def remove(self, key):
        """
        分三种情况:
         1. 删除节点没有子节点, 那么直接删除就可以了
         2. 如果删除节点只有一个子节点, 那么用这个子节点代替就可以了
         3. 如果删除节点有两个子节点, 这时候找到右子节点树的最小节点, 然后把左子节点挂在这个节点左子树位置上, 然后将右子树挂在父节点上
        但是要考虑删除的是不是父节点...
        """
        father = self.root
        node = father
        while node:
            if node.val < key:
                father = node
                node = node.right
            elif node.val > key:
                father = node
                node = node.left
            else:
                break
        # 防止遇到没找到的情况
        assert node and node.val == key
        # 1. 找到的节点没有子节点
        if not node.left and not node.right:
            # node == father是表示删除的是根节点
            if father == node:
                self.root = None
            else:
                if node == father.right:
                    father.right = None
                elif node == father.left:
                    father.left = None
                else:
                    raise "Delete Error 1"
        # 2. 找到的节点只有一个子节点
        # 只有左子树
        elif node.left and not node.right:
            if father == node:
                self.root = node.left
            else:
                if father.right == node:
                    father.right = node.left
                elif father.left == node:
                    father.left = node.left
                else:
                    raise "Delete Error 2-1"
        elif node.right and not node.left:
            if father == node:
                self.root = node.right
            else:
                if father.right == node:
                    father.right = node.right
                elif father.left == node:
                    father.left = node.right
                else:
                    raise "Delete Error 2-2"

        # 3. 找到的节点有两个子节点
        else:
            # 首先找到右子节点的直接后继
            right = node.right
            rightLeft = right
            while rightLeft.left:
                rightLeft = rightLeft.left
            # 然后开始移动
            if father == node:
                self.root = node.right
                rightLeft.left = node.left
            else:
                left = node.left
                rightLeft.left = left
                if node == father.left:
                    father.left = node.right
                elif node == father.right:
                    father.right = node.right
                else:
                    raise "Delete Error 3"

    def find(self, key):
        root = self.root
        if root.val == key:
            return root
        while root:
            if root.val < key:
                root = root.right
            elif root.val > key:
                root = root.left
            else:
                return root
        return None

    def isEmpty(self):
        return self.root == None

    def queueTravel(self):
        if not self.root:
            print("None")
            return
        root = self.root
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

    def postTravel(self):
        if self.root:
            self.travelP(self.root)
            print()
        else:
            print("None")

    def travelP(self, node):
        if not node:
            return
        self.travelP(node.left)
        self.travelP(node.right)
        print(node.val, end=" ")

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def testBinarySearchTree():
    l = [6, 3, 8, 1, 5, 3, 4]
    T = BinarySearchTree()
    for i in l:
        T.insert(TreeNode(i))
        T.queueTravel()
        T.postTravel()
    print("Begin remove:")
    T.remove(6)
    T.queueTravel()
    T.postTravel()
    while not T.isEmpty():
        T.remove(T.root.val)
        T.queueTravel()
        T.postTravel()

testBinarySearchTree()