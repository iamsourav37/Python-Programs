# Program to print all Pronic numbers between 1 to 100

'''
Pronic number

The pronic number can be defined as the number which is a product of two consecutive numbers. Mathematically, the Pronic number can be represented as

N x (N + 1)
'''


def is_pronic_number(number):
    flag = False
    for i in range(1,number):
        if i* (i+1) == number:
            flag = True
            break
    return flag


print("Pronic numbers between 1 to 1000 : ")

for i in range(1,1000):
    if is_pronic_number(i):
        print(i)