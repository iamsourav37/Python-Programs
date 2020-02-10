# Program to print all Happy numbers between 1 to 100


a = int(input("Enter from : "))
b = int(input("Enter upto : "))


def is_happy_number(number):
    sum = rem = 0
    while number != 0:
        rem = number % 10
        sum += rem ** 2
        number //= 10
    return sum


while a <= b:
    result = a
    while result != 1 and result != 4:
        result = is_happy_number(result)

    if result == 1:
        print(a)
    a += 1