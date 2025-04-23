class BinNode:

    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None


class DictBinTree:

    def __init__(self):
        self.root = None

    def search(self, k):
        return self._search(self.root, k)

    def _search(self, x, k):
        if x == None or k == x.key:
            if x == None:
                return False
            else:
                return True

        if k < x.key:
            return self._search(x.left, k)
        else:
            return self._search(x.right, k)

    def insert(self, z):
        return self._insert(self.root, z)

    def _insert(self, T, z):
        x = self.root
        y = None
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        # z.p = y  # because your project does not require storing parent pointers in the tree nodes.
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def orderedTraversal(self):
        return self._orderedTraversal(self.root)

    def _orderedTraversal(self, x):
        result = []
        if x is not None:
            result += self._orderedTraversal(x.left)
            result.append(x.key)
            result += self._orderedTraversal(x.right)
        return result


if __name__ == "__main__":
    first_tree = DictBinTree()
    first_tree.insert(BinNode(5))
    first_tree.insert(BinNode(10))
    first_tree.insert(BinNode(15))
    first_tree.insert(BinNode(2))
    first_tree.insert(BinNode(7))
    first_tree.insert(BinNode(11))
    first_tree.insert(BinNode(16))

    print(first_tree.orderedTraversal())

    print(first_tree.search(8))
