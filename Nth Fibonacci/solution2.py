'''
Author : Dhruv B Kakadiya

'''
# O(n) time | O(n) space

def getNthFib(n, memory = {1: 0, 2: 1}):
    # Write your code here.
    if (n in memory):
        return (memory[n])
    else:
        memory[n] = getNthFib(n - 1, memory) + getNthFib(n - 2, memory)
        return memory[n]