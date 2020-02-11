# Program to print the largest and smallest element present in an array


def find_largest(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if max<arr[i]:
            max = arr[i]
    return max


def find_smallest(arr):
    min = arr[0]
    for i in range(1, len(arr)):
        if min > arr[i]:
            min = arr[i]
    return min


arr = [12,23,34,57,43,323,4,7,8,9,11,37,120,121,123,33,3]
print("Largest element is :",find_largest(arr))
print("Smallest element is :",find_smallest(arr))
