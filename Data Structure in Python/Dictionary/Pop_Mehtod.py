#The Python pop() method removes and returns the value of a specified key from a dictionary. If the key isn't found, you can provide a default value to return instead of raising an error.

d = {'a': 1, 'b': 2, 'c': 3}
v = d.pop('b')
print(v)  

v = d.pop('d', 'Not Found')
print(v)