# 2 sum algorithm solution

numbers = [2, 7, 11, 15, 17, 18, 21]
target = 9

def two_sum(array, target):

    for i in range(len(array)):
        complement_value = target - array[i] #####

        left = i+1
        right = len(array) - 1

        while left <= right:
            mid = (left + right)//2

            if array[mid] == complement_value:
                return i, mid
            elif array[mid] < complement_value:
                left = mid + 1
            else:
                right = mid - 1
    
    return 'no i','no mid'

print(two_sum(numbers, target))