# Program to find the frequency of each element of an array


def frequency_counter(value,full_array):
    count = 0
    for i in full_array:
        if value == i:
            count += 1
    return count

arr = [1, 2, 8, 3, 2, 2, 2, 5, 1]

for i in range(len(arr)):
    print(f"Frequency of {arr[i]} is {frequency_counter(arr[i],arr)}")














