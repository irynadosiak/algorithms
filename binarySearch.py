def binarySearch(array, x):
    l = 0
    r = len(array) - 1
    if r >= l:
        mid = l + (r - l) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch(array, l, mid - 1, x)
        else:
            return binarySearch(array, mid + 1, r, x)
    else:
        return -1


array = [2, 3, 4, 28, 50]
x = 28
if binarySearch(array, x) == -1:
    print("Element is not present in array")
else:
    print("Element is present at index ", binarySearch(array, x))
