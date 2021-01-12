'''
Author : Dhruv B Kakadiya

'''
# O(n) time | O(1) space

def isValidSubsequence(array, sequence):
    # Write your code here.
    arrayInd, seqInd = 0, 0
    while ((arrayInd < len(array)) and (seqInd < len(sequence))):
        if (array[arrayInd] == sequence[seqInd]):
            seqInd += 1
        arrayInd += 1
    return (seqInd == len(sequence))