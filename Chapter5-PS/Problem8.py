# Can you change the value inside a list which is contained in set S

s = {8, 7,12, "Harry", [1,2]}
print(s)

# No, you cannot change the value inside the list because a set cannot contain a list. Lists are mutable (changeable) and sets only allow immutable (unchangeable) elements, so Python will give an error when creating this set.