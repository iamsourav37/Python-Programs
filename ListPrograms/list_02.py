# Python program to swap two elements in a list

# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

def swap_in_list(mylist, pos1, pos2):
  first_element = mylist[pos1]
  second_element = mylist[pos2]

  mylist[pos1] = second_element
  mylist[pos2] = first_element
  




my_list = [10, 12, 20, 18, 21]

print("List : ", my_list)
pos1 = int(input("Enter position one : "))
pos2 = int(input("Enter position two : "))

if (pos1<1 or pos1>len(my_list)) or (pos2<1 or pos2>len(my_list)):
  print("enter in beetween my list index")
  raise Exception("Not in range")

swap_in_list(my_list, pos1-1, pos2-1)

print(f"after swaping {pos1} and {pos2} in list")
print(my_list)


