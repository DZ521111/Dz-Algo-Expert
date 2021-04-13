def get_result_bound_length(main_string):
    current_pattern = main_string[-1:]
    pattern_count = 0
    for i in range(len(main_string)-1,-1,-1):
        if main_string[i] != current_pattern:
            pattern_count+=1
            if i > 0:
                current_pattern = main_string[i-1]
    return pattern_count+1


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


for _ in range(int(input())):
    S = input()
    result_bit_length = get_result_bound_length(S)
    start,end = 0,(2**result_bit_length) - 1
    if result_bit_length > 1:
        start = 2**(result_bit_length-1)
    
    for i in range( start,end):
        bin_string = bin(i)[2:]
        if not is_subsequence(S,bin_string):
            print(bin_string)
            break
