def average(arr):
    distinct = set(arr)                 # remove duplicates
    return sum(distinct) / len(distinct)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(f"{result:.3f}")
