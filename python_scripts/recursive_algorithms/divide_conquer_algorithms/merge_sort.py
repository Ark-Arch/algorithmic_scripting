# Timsort could help reduce space complexity
# TImsort is a variation of merge sort

arr = [5, 2, 9, 1, 5, 6]

def merge_sort(array):
    # base case
    if len(array) <= 1:
        return array
    else:
        mid = len(array)//2
        array_one = array[:mid]
        array_two = array[mid:]
        array_one = merge_sort(array_one)
        array_two = merge_sort(array_two)
        return merge_arrays(array_one, array_two)

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

print(merge_sort(arr))