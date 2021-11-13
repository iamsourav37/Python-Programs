# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.



def main():
    min_limit = 2000
    max_limit = 3200

    output_list = []
    for i in range(min_limit, max_limit+1):
        if (i % 7 == 0) and (i % 5 != 0):
            print(i, end=", ")



if __name__ == "__main__":
    main()
