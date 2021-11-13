
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be :40320


def factorial(num):
    result = 1
    while num:
        result *= num
        num -= 1
    return result


def main():
    num = int(input("Enter a number : "))
    result = factorial(num)
    print(result)


if __name__ == "__main__":
    main()