from itertools import product

# Read input
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute cartesian product
result = product(A, B)

# Print output in required format
for item in result:
    print(item, end=' ')
