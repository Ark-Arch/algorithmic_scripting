def selection_sort(array):
    for i in range(len(array)):
        min_index = i # set the first element of the unsorted array to be the minimum element
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j  # update the minimum element's index
        array[i], array[min_index] = array[min_index], array[i]
    
    return array

array = [234,1,5,2,7,9,0,1,5,6,8,7,4,3]
sorted_array = selection_sort(array)

print(sorted_array)