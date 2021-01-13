'''
Author : Dhruv B Kakadiya

'''
# O(n) time | O(h) space

def nodeDepths(root):
    # Write your code here.
	depthSums = 0
    memoryNodes = [{"node": root, "depth": 0}]
	while (len(memoryNodes) > 0):
		nodes = memoryNodes.pop()
		currNode, depth = nodes["node"], nodes["depth"]
		if (currNode is None):
			continue
		depthSums += depth
		memoryNodes.append({"node": currNode.left, "depth": depth + 1})
		memoryNodes.append({"node": currNode.right, "depth": depth + 1})
	return depthSums

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

