# Declares an initial list with 5 values
List1 = [1,2,3,4,5]

# Unpacks this list into 5 separate variables
a,b,c,d,e = List1

# Prints both the list and one of the unpacking variables
print(List1)
print(a)

# Changes the value of a to 6
a = 6

# Prints both the list and a, and we can see that changing a does not change the corresponding value in the list
print(a)
print(List1)

# Changes the value of one list entry to nine
List1[1] = 9

# Prints the list and the corresponding unpacking variable to show that changing the unpacking
# variable does not change the list value
print(List1)
print(b)

# We conclude that this method does not just create a variable that points to the same location in space, but rather
# fills new separately stored variables with values from the list
