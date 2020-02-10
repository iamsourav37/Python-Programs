# Program to Check Harshad number

'''
A number is said to be the Harshad number if it is divisible by the sum of its digit.

For example, if number is 156, then sum of its digit will be 1 + 5 + 6 = 12. Since 156 is divisible by 12. So, 156 is a Harshad number.

Some of the other examples of Harshad number are 8, 54, 120, etc.
'''

def sum_of_digit(number):
        sum = 0
        while number != 0:
                sum += (number%10)
                number //= 10
        return sum


def is_harshed_number(number):
        divisor = sum_of_digit(number)
        if number % divisor == 0:
                return True
        else:
                return False


number = int(input("Enter any number : "))
if is_harshed_number(number):
        print(number,' ia harshed number')
else:
        print(number,'is not harshed number')







