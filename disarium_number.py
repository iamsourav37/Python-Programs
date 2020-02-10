# Program to Check Disarium number
'''
Disarium number

A number is said to be the Disarium number when the sum of its digit raised to the power of their respective positions is equal to the number itself.

For example, 175 is a Disarium number as follows

11 + 72 + 53 = 1 + 49 + 125 = 175
Some of the other examples of Disarium number are 89, 135, 518 etc.
'''

number = int(input("Enter any number : "))

def count_digit(number):
    count = 0
    while number != 0:
            count += 1
            number //= 10
    return count


def is_disarium_number(number):
    power = count_digit(number)
    temp = number
    sum = 0
    while temp != 0:
            remainder = temp %10
            sum += remainder**power
            power -= 1
            temp //= 10
    if sum == number:
        return True
    else:
        return False


if is_disarium_number(number):
        print(number, 'is a disarium number')
else:
    print(number, 'is not a disarium number')
