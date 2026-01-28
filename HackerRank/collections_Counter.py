from collections import Counter

# number of shoes
n = int(input())

# list of shoe sizes
sizes = list(map(int, input().split()))

# count available shoes
stock = Counter(sizes)

# number of customers
m = int(input())

total_earned = 0

for _ in range(m):
    size, price = map(int, input().split())
    
    # if shoe size available
    if stock[size] > 0:
        total_earned += price
        stock[size] -= 1   # decrease stock after selling

print(total_earned)
