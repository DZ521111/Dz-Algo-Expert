'''
Author : Dhruv B Kakadiya

'''
# O(nlog(n)) time | O(1) space

def twoNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
	front_side, back_side = 0, len(array) - 1
	while (True):
		if ((array[front_side] + array[back_side]) == targetSum):
			return ([array[front_side], array[back_side]])
		elif ((array[front_side] + array[back_side]) < targetSum):
			front_side += 1
			if (front_side > back_side):
				return ([])
		elif ((array[front_side] + array[back_side]) > targetSum):
			back_side -= 1
			if (front_side > back_side):
				return ([])
