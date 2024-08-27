# Leetcode 27
# nums = [3,2,2,3]

# remove the elements that are value in the array
# return the array to consist of only the elements that are not the value
# return the number of such elements not the value
def remove_element(array, value):
    left = 0
    right = len(array) - 1

    while ( left <= right ):
        if array[right] != value:
            array[left], array[right] = array[right], array[left]
            left += 1
        else:
            nums.pop()
            right -= 1
    
    return (len(nums), nums)

nums = [1]
print(remove_element(nums, 1))