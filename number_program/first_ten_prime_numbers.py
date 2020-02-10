# Program to print the first 10 prime numbers
def is_prime(number):
    flag = True
    for i in range(2,number//2+1):
        if number % i == 0:
            flag = False
            break
    return flag

count = 0
i = 2
while count != 10:
    if is_prime(i):
        print(i)
        count += 1
    i += 1

