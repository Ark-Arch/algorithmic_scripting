# two point sum using the 2-pointer technique
# time complexity = O(n)
# space complexity = O(1)

def two_sum(array, target_sum):
    left = 0
    right = len(array) - 1

    while (left < right):
        summation = array[left] + array[right]

        if summation == target_sum:
            return [left, right]
        elif summation < target_sum:
            left += 1
        else:
            right -= 1
    return "does not exist"

numbers = [2, 7, 11, 15, 17, 18, 21]
target = 23

print(two_sum(numbers, target))