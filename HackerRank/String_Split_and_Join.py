def split_and_join(line):
    # Split the string by space
    words = line.split(" ")
    
    # Join the words using hyphen
    result = "-".join(words)
    
    return result


# Input
line = input().strip()

# Output
print(split_and_join(line))
