d = {}
n = int(input("How many items: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print(d)


# Integer value dictionary

d = {}
n = int(input("How many items: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

print(d)
