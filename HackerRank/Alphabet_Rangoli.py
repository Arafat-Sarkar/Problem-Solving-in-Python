def print_rangoli(size):
    import string
    
    alphabets = string.ascii_lowercase
    width = 4 * size - 3

    # Top half (including middle)
    for i in range(size):
        left = alphabets[size-1:size-i-1:-1]
        right = alphabets[size-i-1:size]
        line = "-".join(left + right)
        print(line.center(width, "-"))

    # Bottom half
    for i in range(size-2, -1, -1):
        left = alphabets[size-1:size-i-1:-1]
        right = alphabets[size-i-1:size]
        line = "-".join(left + right)
        print(line.center(width, "-"))
