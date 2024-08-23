
# BRUTE FORCE SOLUTION ==> O(n)
#####################################################
def two_sum(array, target_value):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target_value:
                return i,j
######################################################

array = [0,1,2,32,4,5]
target_value = 6

numbers = [2,7,11,15]
target = 9

i,j = two_sum(numbers, target)

print(i)
print(j)

