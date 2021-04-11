'''
Author : Dhruv B Kakadiya

'''
class BSTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def addVlaue(root, value):
    if root is None:
        return BSTree(value)
    else:
        if (root.value < value):
            root.right = BSTree(root.right, value)
        elif (root.value > value):
            root.left = BSTree(root.left, value)
        else:
            return root


if __name__ == "__main__":
    r = BSTree(10)
    r = BSTree(r, 5)
    r = BSTree(r, 15)
    r = BSTree(r, 2)
    r = BSTree(r, 5)
    r = BSTree(r, 13)
    r = BSTree(r, 22)
    r = BSTree(r, 1)
    r = BSTree(r, 14)
    target = 12
    print(findClosestValueOfBst(r, target))