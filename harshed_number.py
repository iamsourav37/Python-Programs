# Program to Check Harshad number


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







