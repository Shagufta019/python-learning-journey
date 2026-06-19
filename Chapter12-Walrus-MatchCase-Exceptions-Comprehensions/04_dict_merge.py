dict1 = {'a': 1,
         'b' : 3}

dict2 = {'b': 2,
         'c' : 6}

merged = dict1 | dict2

print(merged) # Output: {'a': 1, 'b': 2, 'c': 6}