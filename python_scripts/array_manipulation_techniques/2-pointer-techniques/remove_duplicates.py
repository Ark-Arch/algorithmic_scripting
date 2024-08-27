# leetcode 26
# remove duplicates from sorted array

def remove_duplicates(array):

    left = 0
    right = 0

    while (right < len(array)):
        if array[right] != array[left]:
            left +=1
            array[left], array[right] = array[left], array[right]
        right += 1

    return left + 1