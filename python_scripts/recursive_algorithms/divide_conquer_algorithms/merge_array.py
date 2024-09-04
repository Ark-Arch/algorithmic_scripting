array_one = [1,3,5,7]
array_two = [1,2,3,4,6,8,8]

def merge_arrays(array_one, array_two):
    one_pointer = 0
    two_pointer = 0

    len_one = len(array_one)
    len_two = len(array_two)

    merged_array = []

    while(one_pointer < len_one and two_pointer < len_two):
        if array_one[one_pointer] <= array_two[two_pointer]:
            merged_array.append(array_one[one_pointer])
            one_pointer += 1
        else:
            merged_array.append(array_two[two_pointer])
            two_pointer += 1
    
    while (one_pointer < len_one):
        merged_array.append(array_one[one_pointer])
        one_pointer += 1
    
    while (two_pointer < len_two):
        merged_array.append(array_two[two_pointer])
        two_pointer += 1
    
    return merged_array

print(merge_arrays(array_one, array_two))