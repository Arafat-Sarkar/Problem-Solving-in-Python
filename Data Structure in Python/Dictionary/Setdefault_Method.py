# The setdefault() method in Python is used with dictionaries to:

# Return the value of a specified key if it exists.
# If the key does not exist, it adds the key with a default value and returns that default.

d = {'a': 97, 'b': 98}
print("setdefault() returned:", d.setdefault('b', 99))
print("After using setdefault():", d)