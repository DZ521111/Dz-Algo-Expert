'''
Author : Dhruv B Kakadiya

'''
# O(n) time | O(h) space

def nodeDepths(root, depth = 0):
    # Write your code here.
    if (root is None):
        return (0)
    return (depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1))


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
