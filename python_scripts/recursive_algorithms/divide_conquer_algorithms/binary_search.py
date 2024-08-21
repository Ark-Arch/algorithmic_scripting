
def binary_search(array, left_pointer, right_pointer, number):
    """
    inputs:
        array: a sorted array from which to search a value from
        left_pointer: left index pointer
        right_pointer: right index pointer
        number: the value which is to be sought from the sorted array
    return:
        a recursive return.
    """

    # Base Case 1
    if left_pointer > right_pointer:
        return "Unfortunately, the number does not exist in the array"

    # find the mid pointer
    mid_pointer = (left_pointer + right_pointer)//2

    # Base Case 2
    if number == array[mid_pointer]:
        return mid_pointer

    # divide the problems
    if (number > array[mid_pointer]):
        return binary_search(array, mid_pointer+1, right_pointer, number)
    else:
        return binary_search(array, left_pointer, mid_pointer-1, number)

array = [0, 1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 234]

print(binary_search(array, 0, len(array)-1, 7))