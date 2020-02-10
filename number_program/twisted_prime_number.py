# Program to determine whether a given number is a twisted prime number

'''
A number is called a twisted prime number if it is a prime number and reverse( 13 ->31 , 17 -> 71 ) of this number is also a prime number.

Examples: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79
'''


def is_prime(number):
    flag = True
    for i in range(2,number//2+1):
        if number % i == 0:
            flag = False
            break
    return flag


def reverse_number(number):
    reverse = 0
    while number != 0:
        reverse = reverse*10 + number%10
        number //= 10
    return reverse


number = int(input("Enter any number : "))
if is_prime(number):
    reverse = reverse_number(number)
    print('reversed number :',reverse)
    if is_prime(reverse):
        print(number,"is a twisted prime number")
    else:
        print(number,"is a prime number but not twisted prime number")
else:
    print(number, "is not a prime number")

