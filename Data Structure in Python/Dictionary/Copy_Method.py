# Python Dictionary copy() method returns a shallow copy of the dictionary.

original = {1: 'arafat', 2: 'rifat'}

# copying using copy() function
new = original.copy()

# removing all elements from the list
# Only new list becomes empty as copy()
# does shallow copy.
new.clear()

print('new: ', new)
print('original: ', original)