# popitem() method in Python is used to remove and return the last key-value pair from the dictionary. It is often used when we want to remove a random element, particularly when the dictionary is not ordered.

d = {1: '001', 2: '010', 3: '011'}

# Using popitem() to remove and return the last item
res = d.popitem()
print(res)
print(d)