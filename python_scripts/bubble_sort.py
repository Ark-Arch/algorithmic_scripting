
unsorted_array = [2,8,1,9,3,5,1,3,7,6,2,9]

def bubble_sort(A):
    x = len(A)
    for i in range(len(A)):
        for j in range(0,len(A)): 
            if j!=len(A)-1 and A[j+1] < A[j]:
                tmp = A[j]
                A[j] = A[j+1]
                A[j+1] = tmp
        x-=1

    return A

sorted_array = bubble_sort(unsorted_array)

print(sorted_array)


