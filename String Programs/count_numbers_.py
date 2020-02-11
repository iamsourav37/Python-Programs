# Program to count numbers in a string


def count_number(str):
    count = 0
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    for i in str:
        if i in numbers:
            count += 1
    return count


str = "Hello all932 how 2334 you 0997"
str2 = "hello 123"
print("Number Count :",count_number(str))
print("Number Count :",count_number(str2))

