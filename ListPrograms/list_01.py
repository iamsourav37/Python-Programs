# Python program to interchange first and last elements in a list

my_list = [21, 12, 20, 29, 38]

# first_element = my_list[0]
# last_element = my_list[-1]

# my_list[0] = last_element
# my_list[-1] = first_element

# print(my_list)


my_list[0] , my_list[-1] = my_list[-1], my_list[0]
print(my_list)
