# Program to print the elements of an array present on odd position


arr = [12,23,34,57,43,323,4,7,8,9,11,37,120,121,123,333,1]

print("Array length :",len(arr))
for i in range(1,len(arr),2):
    print(f'arr[{i}] = {arr[i]}')


