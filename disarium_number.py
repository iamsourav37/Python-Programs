# Program to Check Disarium number

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
