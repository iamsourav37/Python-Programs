# Program to left rotate the elements of an array

'''
arr = [1, 2, 3, 4, 5]
Here, n determine the number of times an array should be rotated
n = 3
'''

arr = ['This' ,'program','is','written','by','Sourav','Ganguly','or iamSourav37']
rotation_number = int(input('Enter the number of times should be rotated : '))
if rotation_number > len(arr):
    print(f"{rotation_number} elements is not present in the array")
    exit()
another_arr = arr[:rotation_number]
del arr[:rotation_number]
arr += another_arr
print(arr)



