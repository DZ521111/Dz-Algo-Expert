'''
Author : Dhruv B kakadiya

'''

import io, os

def get_result_bound_length(main_string):
    current_pattern = main_string[-1:]
    pattern_list = []
    pattern_count = 0
    for i in range(len(main_string)-1,-1,-1):
        pattern_list.append(pattern_count)
        if main_string[i] != current_pattern:
            pattern_count+=1
            if i > 0:
                current_pattern = main_string[i-1]
    pattern_list.append(pattern_count)
    pattern_list.reverse()
    return pattern_list

def is_subsequence(main_string,test_string):
    i=0
    #print(f"ms-{main_string}, ts- {test_string} ")
    for j in range(len(main_string)):
        if test_string[i]==main_string[j]:
            i+=1

        if i == len(test_string):
            #print("done")
            return True
        #print(j,i)
    if i == len(test_string):
        return True
    else:
        return False

if __name__ == '__main__':
    #input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    rearBit0 = [None for _ in range(pow(10, 2))]
    rearBit1 = [None for _ in range(pow(10, 2))]
    superArray = []
    mex = ""
    lastIdx = -1
    for _ in range(int(input())):
        binaryString = input()
        stringLen = len(binaryString)
        for i in range(stringLen):
            if (binaryString[i] == '0'):
                #print("Again")
                for j in range(lastIdx + 1, i + 1):
                    #print(f"j is {j}")
                    rearBit0[j] = i
                lastIdx = i

        #print(f"rearBit0 is :- {rearBit0}\n")

        for i in range(lastIdx + 1, stringLen + 3):
            rearBit0[i] = stringLen
        if (rearBit0[0] == stringLen):
            print(0)
            continue

        print(f"rearBit0 is :- {rearBit0}\n")

        lastIdx = -1
        for i in range(stringLen):
            if (binaryString[i] == "1"):
                for j in range(lastIdx + 1, i + 1):
                    rearBit1[j] = i
                lastIdx = i

        #print(f"rearBit1 is :- {rearBit1}\n")

        for i in range(lastIdx + 1, stringLen + 3):
            rearBit1[i] = stringLen

        print(f"rearBit1 is :- {rearBit1}\n")

        superArray = get_result_bound_length(binaryString)
        n = len(superArray)
        for i in range(n, n + 4):
            superArray.append(0)
        print(superArray)

        length = superArray[0] + 1
        currIdx = rearBit1[0] + 1
        mex += "1"
        for i in range(1, length):
            if (currIdx >= stringLen):
                mex += "0"
                continue
            if (rearBit0[currIdx] >= stringLen):
                mex += "0"
                currIdx = rearBit0[currIdx] + 1
                continue
            if (superArray[rearBit0[currIdx] + 1] < length - i - 1):
                mex += "0"
                currIdx = rearBit0[currIdx] + 1
            else:
                mex += "1"
                currIdx = rearBit1[currIdx] + 1
        if (not is_subsequence(binaryString, mex)):
            print(mex)
            continue
        else:
            mex = ""
            length = superArray[0] + 2
            currIdx = rearBit1[0] + 1
            mex += "1"
            for i in range(1, length):
                print(f" curr index is :- {currIdx}")
                if (rearBit0[currIdx] >= stringLen):
                    mex += "0"
                    currIdx = rearBit0[currIdx] + 1
                    continue
                if (currIdx >= stringLen):
                    mex += "0"
                    continue
                if (superArray[rearBit0[currIdx] + 1] < length - i - 1):
                    mex += "0"
                    currIdx = rearBit0[currIdx] + 1
                else:
                    mex += "1"
                    currIdx = rearBit1[currIdx] + 1
            if (not is_subsequence(binaryString, mex)):
                print(mex)
                continue
