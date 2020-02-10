# Program to determine whether a given number is a Deficient number
'''
The deficient number can be defined as the number for which the sum of the proper divisors is lesser than the number itself.
For example, the number 21 with its proper divisors (1, 3 and 7) has sum (11) lesser than itself.
'''


def sum_of_divisor(number):
    sum = 0

    for i in range(1,number//2+1):
        if number % i == 0:
            sum += i
    return sum

number = int(input("Enter any number :"))
sum = sum_of_divisor(number)

if sum<number:
    print(number,"is a Deficient number")
else:
    print(number,"is not a Deficient number")




