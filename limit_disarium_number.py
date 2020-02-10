# Program to print all Disarium numbers between any range

a = int(input("Enter from : "))
b = int(input("Enter upto : "))


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


print(f"Disarium number between {a} to {b} :")
while a <= b:
    if is_disarium_number(a):
        print(a)
    a += 1


