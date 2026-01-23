# Read input
N, M = map(int, input().split())

# Top part
for i in range(1, N, 2):
    pattern = ".|." * i
    print(pattern.center(M, "-"))

# Middle part
print("WELCOME".center(M, "-"))

# Bottom part
for i in range(N-2, 0, -2):
    pattern = ".|." * i
    print(pattern.center(M, "-"))
