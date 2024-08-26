# A CASE WHERE THE ARRAY IS NOT BEEN SORTED

array = [3,2,4]
target = 6

def two_sum(array, target_sum):

    # preserve the keys
    array = [(num, index) for index, num in enumerate(array)]   # O(n)

    #sort the array
    array.sort(key= lambda x:x[0]) # O(nlogn)

    left = 0
    right = len(array) - 1

    while(left < right): #O(n)
        summation = array[left][0] + array[right][0]

        if summation == target_sum:
            return [array[left][1], array[right][1]]
        elif summation > target_sum:
            right -= 1
        else:
            left += 1
    
print(two_sum(array, target))    
