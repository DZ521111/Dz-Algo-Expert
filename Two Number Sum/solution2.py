'''
Author : Dhruv B Kakadiya

'''
# O(n) time | O(n) space

def twoNumberSum(array, targetSum):
    # Write your code here.
    numHash = {}
    for num in array:
        y = targetSum - num
        if (y in numHash):
            return ([y, num])
        else:
            numHash[num] = True
    return ([])