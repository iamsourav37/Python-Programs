# Program to find the frequency of each element of an array


def frequency_counter(value,full_array):
    count = 0
    for i in full_array:
        if value == i:
            count += 1
    return count


arr = [1, 2, 8, 3, 2, 2, 2, 5, 1]
unique_values = set(arr)

for i in unique_values:
    print(f"Frequency of {i} is {frequency_counter(i,arr)}")














