# Program to print the duplicate elements of an array



def duplicate_elements(arr):
    checked = []
    print("Array elements are %s"%arr)
    print("Duplicate elements are : ")
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j] and arr[i] not in checked:
                checked.append(arr[i])
                print(arr[i])


arr = [2,3,4,2,3,1,45,60,6,60,8,5,6,2]
duplicate_elements(arr)






