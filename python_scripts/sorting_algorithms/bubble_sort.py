def ascending_order(x,y):
    if x < y:
        x, y = y, x
    return x, y
def descending_order(x, y):
    if x > y:
        x, y = y, x
    return x,y

def bubble_sort(array, order="ascending"):
    for i in range(len(array)):
        for j in range(1, len(array)):
            if order == "ascending":
                array[j], array[j-1] = ascending_order(array[j], array[j-1])
            elif order == "descending":
                array[j], array[j-1] = descending_order(array[j], array[j-1])
    return array


array = [0, 1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 234]
sorted_array = bubble_sort(array, "ascending")

print(sorted_array)