# Python Dictionary update() method updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs.

# update() method in Dictionary

# Dictionary with three items
d1 = {'A': 'arafat', 'B': 'For', }
d2 = {'B': 'rifat', 'C': 'Python'}


# update the value of key 'B'
d1.update(d2)

# using keyword arguments
d1.update(A='Hello')

print(d1)