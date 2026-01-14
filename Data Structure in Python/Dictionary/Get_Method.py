# Python Dictionary get() Method returns the value for the given key if present in the dictionary. 

# Python Dictionary get() Method Syntax:

# Syntax : Dict.get(key, Value)

# Parameters: 
# key: The key name of the item you want to return the value from
# Value: (Optional) Value to be returned if the key is not found. The default value is None.
# Returns: Returns the value of the item with the specified key or the default value.

#Code 

test_dict = {'Gfg' : {'is' : 'best'}}
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
  
# using nested get()
# Safe access nested dictionary key
res = test_dict.get('Gfg', {}).get('is')
  
# printing result
print("The nested safely accessed value is :  " + str(res))