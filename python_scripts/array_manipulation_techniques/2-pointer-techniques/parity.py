# LEET CODE 905
# arrange the even numbers to start the array, while the odd is left behind.

#Input: nums = [3,1,2,4]
#Output: [2,4,3,1]
#Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

def parity(array):
    left = 0
    right = len(array) - 1

    while (left < right):
        if array[right] % 2 == 0:
            array[left], array[right] = array[right], array[left]
            left += 1
        else:
            right -= 1
    
    return array

nums = [3,1,2,4]
print(parity(nums))