# The copy() method in Python is used to create a shallow copy of a list.

a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]