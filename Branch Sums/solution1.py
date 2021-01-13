'''
Author : Dhruv B Kakadiya

'''
# O(n) time | O(n) space | n is number of nodes

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    # Write your code here.
	sums = []
	branchSumsCalculation(root, 0, sums)
	return sums

def branchSumsCalculation(node, currSum, sums):
	if (node is None):
		return

	newCurrSum = currSum + node.value
	if ((node.left is None) and (node.right is None)):
		sums.append(newCurrSum)
		return

	branchSumsCalculation(node.left, newCurrSum, sums)
	branchSumsCalculation(node.right, newCurrSum, sums)