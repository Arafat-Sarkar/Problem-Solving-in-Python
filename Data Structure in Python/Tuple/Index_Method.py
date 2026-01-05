# The Index() method returns the first occurrence of the given element from the tuple.

# Syntax:  tuple.index(element, start, end)

# Creating tuples
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)

# getting the index of 3
res = Tuple.index(3)
print('First occurrence of 3 is', res)

# getting the index of 3 after 4th
# index
res = Tuple.index(3, 4)
print('First occurrence of 3 after 4th index is:', res)