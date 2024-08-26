# move the zeroes in an array to the back of the array.
# implement the algorithm in place without making a copy of the array.
# while maintaining the relative order of the non-zero elements.

nums = [6,0,1,0,3,12, 0,0]

def move_zeroes(array):
    left = 0
    right = 0

    while (right < len(array)):
        if array[right] != 0:
            array[left], array[right] = array[right], array[left]
            left += 1
        right += 1

    return array

print(move_zeroes(nums))