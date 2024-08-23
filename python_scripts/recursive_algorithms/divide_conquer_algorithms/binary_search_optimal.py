

def binary_search(array, target_value):
    left = 0
    right = len(array) - 1

    while (left <= right):
        mid = (left + right)//2

        if array[mid] == target_value:
            return mid
        else:
            if array[mid] > target_value:
                right = mid - 1
            else:
                left = mid + 1
    
    return "the target value does not exist in the list"

array = [0, 1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 234]
arr = [7]

print(binary_search(arr, 7))