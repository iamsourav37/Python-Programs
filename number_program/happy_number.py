# Program to Check Happy number
'''
Happy number

The happy number can be defined as a number which will yield 1 when it is replaced by the sum of the square of its digits repeatedly. If this process results in an endless cycle of numbers containing 4, then the number is called an unhappy number.

For example, 32 is a happy number as the process yields 1 as follows

32 + 22 = 13
12 + 32 = 10
12 + 02 = 1
Some of the other examples of happy numbers are 7, 28, 100, 320 and so on.

The unhappy number will result in a cycle of 4, 16, 37, 58, 89, 145, 42, 20, 4, ....

To find whether a given number is happy or not, calculate the square of each digit present in number and add it to a variable sum. If resulting sum is equal to 1 then, given number is a happy number. If the sum is equal to 4 then, the number is an unhappy number. Else, replace the number with the sum of the square of digits.
'''
def is_happy_number(number):
        sum = rem = 0

        while number != 0:
                rem = number %10
                sum += rem**2
                number //= 10
        return sum


number = int(input("Enter any number : "))

result = number

while result != 1 and result != 4:
        result = is_happy_number(result)

if result == 1:
        print(number,'is a Happy number')
else:
    print(number,'is an unhappy number')

