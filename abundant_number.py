# Program to determine whether a given number is an abundant number


'''
The abundant number can be called as an excessive number and defined as the number for which the sum of its proper divisors is greater than the number itself.

A first abundant number is the integer 12 having the sum (16) of its proper divisors (1, 2, 3, 4, 6) which is greater than itself (12).

Examples: 12, 18, 20, 24, 30, 36
'''


def sum_of_divisor(number):
    sum = 0

    for i in range(1,number//2+1):
        if number % i == 0:
            sum += i
    return sum

number = int(input("Enter any number :"))
sum = sum_of_divisor(number)
print(sum)
if sum>number:
    print(number,"is an abundant number")
else:
    print(number,"is not an abundant number")



