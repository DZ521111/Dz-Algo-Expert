'''
Author : Dhruv B Kakadiya

'''


def isValidSubsequence(array, sequence):
    # Write your code here.
	currIndex = -1
	for num in sequence:
		if (array.count(num) >= sequence.count(num)):
			indexNum = array.index(num)
			array[indexNum] = False
		else:
			return (False)
		if (indexNum > currIndex):
			currIndex = indexNum
		else:
			return (False)
	else:
		return (True)