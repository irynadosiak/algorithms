def linear_search(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = [2, 3, 4, 28, 50]
x = 28
n = len(array)
if linear_search(array, n, x) == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", linear_search(array, n, x))
