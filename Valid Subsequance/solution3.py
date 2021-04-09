def isValidSubsequence(array, sequence):
    # Write your code here.
	ind, flag = 0, False
    for ele in sequence:
		for i in range(ind, len(array)):
			if (ele == array[i]):
				flag = True
				ind = i + 1
				break
		else:
			return (False)
	else:
		return (True)