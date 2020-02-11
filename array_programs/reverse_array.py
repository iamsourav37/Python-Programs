# Program to print the elements of an array in reverse order

arr = [1, 2, 3, 4, 5]

print("Original array : ",arr)

# reversing the array
reverse = []
for i in range(len(arr)-1,-1,-1):
    reverse.append(arr[i])


print(reverse)



