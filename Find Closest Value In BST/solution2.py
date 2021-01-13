'''
Author : Dhruv B Kakadiya

'''
# O(log(n)) time | O(1) space | iterative

def findClosestValueInBst(tree, target):
    # Write your code here.
    closest = tree.value
    currNode = tree
    while (currNode is not None):
        if (abs(target - currNode.value) < abs(closest - target)):
            closest = currNode.value
        if (target < currNode.value):
            currNode = currNode.left
        elif (target > currNode.value):
            currNode = currNode.right
        else:
            return closest
	return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
