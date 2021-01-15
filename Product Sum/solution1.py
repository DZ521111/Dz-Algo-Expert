# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, multiplier = 1):
    # Write your code here.
	pSum = 0
	for ele in array:
		if (type(ele) == list):
			pSum += productSum(ele, multiplier + 1)
		else:
			pSum += ele
	return (multiplier * pSum)