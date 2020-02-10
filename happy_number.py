# Program to Check Happy number

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

