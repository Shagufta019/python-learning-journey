# Check that a tuple type can not be changed in python.

a = (34, 234, "Harry", 45.7, True)

a[2] = "Larry" #TypeError: 'tuple' object does not support item assignment