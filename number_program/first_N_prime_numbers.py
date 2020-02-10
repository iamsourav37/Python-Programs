# Program to print the first N prime numbers
def is_prime(number):
    flag = True
    for i in range(2,number//2+1):
        if number % i == 0:
            flag = False
            break
    return flag


limit = int(input("Enter range : "))
number = 2
print(f"First {limit} natural numbers are : ")
while limit > 0:
    if is_prime(number):
        print(number)
        limit -= 1
    number += 1


