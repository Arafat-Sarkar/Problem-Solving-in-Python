#Python dictionary fromkeys() function returns the dictionary with key mapped and specific value.

# Syntax : fromkeys(seq, val)

# Parameters :
# seq : The sequence to be transformed into a dictionary.
# val : Initial values that need to be assigned to the generated keys. Defaults to None.
# Returns : A dictionary with keys mapped to None if no value is provided, else to the value provided in the field. 



seq = {'a', 'b', 'c', 'd', 'e'}

# creating dict with default values as None
res_dict = dict.fromkeys(seq)

print("The newly created dict with None values : " + str(res_dict))

# creating dict with default values as 1
res_dict2 = dict.fromkeys(seq, 1)

print("The newly created dict with 1 as value : " + str(res_dict2))