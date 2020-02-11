#  Program to print the elements of an array present on even position

arr = [12,23,34,57,43,323,4,7,8,9,11,37,120,121,123,333,1]

print("Printing the elements present on even position : ")
print('"Method 1"')
for i in range(len(arr)):
    if i%2==0:
        print(f'arr[{i}] = {arr[i]}')


print('"Method 2"')
for i in range(0,len(arr),2):
    print(f'arr[{i}] = {arr[i]}')













