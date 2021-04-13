'''
Author : Dhruv B Kakadiya

'''
def binarySearch(array, target):
    # Write your code here.
	front, rear = 0, len(array)
	mid = search(array, target, front, rear - 1)
	return mid

def search(array, target, front, rear):
	if (front > rear):
		return (-1)
	mid = (front + rear) // 2
	if (array[mid] == target):
		return mid
	elif (array[mid] < target):
		return search(array, target, mid + 1, rear)
	elif (array[mid] > target):
		return search(array, target, front, mid - 1)