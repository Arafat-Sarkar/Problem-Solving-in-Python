from itertools import permutations

s, k = input().split()
k = int(k)

# sort string to ensure lexicographic order
s = sorted(s)

for p in permutations(s, k):
    print("".join(p))
